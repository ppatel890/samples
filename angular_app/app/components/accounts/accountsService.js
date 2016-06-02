'use strict'

/* Account Services */

var accountServices = angular.module('accountsServices', ['ngResource']);

accountServices.factory('Account', ['$resource',
  function($resource){
    return $resource('static/app/components/accounts/:accountId.json', {}, {
      query: {method:'GET', params:{accountId:'accounts'}, isArray:true}
    });
  }]);
