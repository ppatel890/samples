import os
import csv
from datetime import datetime, timedelta
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ads.base_settings')

import django
django.setup()

from django.db.models import Count
from django.core.mail import EmailMessage

from common.models.selfserve import JobPost
from ads.resumes.models import ApplyTracking

def daily_applicants():
    """
    Send an email with daily and total apply count for each active job
    """

    today = datetime.now().date()
    yest = today - timedelta(1)

    jobs = JobPost.objects.filter(status='active', publisher_id=1)

    # refind_keys are unique key for jobs accross multiple dbs
    refind_keys = list(jobs.values_list('refind_key', flat=True))

    applies = ApplyTracking.objects.values('refind_key').annotate(
        total_applies=Count('refind_key')).filter(refind_key__in=refind_keys)
    daily_applies = applies.filter(created__gte=yest, created__lt=today)

    total_applies = {a['refind_key']: a['total_applies'] for a in applies}
    daily_applies = {a['refind_key']: a['total_applies'] for a in daily_applies}

    apply_data = []
    for refind_key in refind_keys:
        apply_data.append({
            'refind_key': refind_key,
            'total_applies': total_applies.get(refind_key),
            'daily_applies': daily_applies.get(refind_key),
            })


    field_names = ['refind_key', 'total_applies', 'daily_applies']
    output_csv_file = '/home/pavan/daily_applicants' + yest.strftime('%m_%d-%y') + '.csv'

    with open(output_csv_file, 'w') as output_file:
        csvwriter = csv.writer(output_file, delimiter=',', lineterminator='\n')
        csvwriter.writerow(field_names)
        csvwriter = csv.DictWriter(
            output_file, delimiter=',', lineterminator='\n',
            fieldnames=field_names, extrasaction='ignore')

        for row in apply_data:
            csvwriter.writerow(row)

    email_recipients = ['pavan@simplyhired.com']

    subject = 'SimplyPost Daily Applicants'
    body_text = 'Applicants for %s' % yest.strftime('%D')

    email = EmailMessage(subject=subject,
                         body=body_text,
                         from_email='Reporting <no-reply@simplyhired.com>',
                         to=email_recipients)

    email.mimetype = 'text/csv'
    email.attach_file(output_csv_file)
    email.send()

    return

if __name__ == '__main__':
    daily_applicants()
