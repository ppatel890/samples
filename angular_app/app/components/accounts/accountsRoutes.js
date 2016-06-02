'use strict';

var enterpriseApp = angular.module('enterpriseApp');

enterpriseApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/accounts', {
        templateUrl: 'static/app/components/accounts/accountsViews/accounts-list.html',
        controller: 'AccountListCtrl'
      }).
      when('/accounts/create', {
        templateUrl: 'static/app/components/accounts/accountsViews/accounts-create.html',
        controller: 'AccountCreateCtrl'
      }).
      when('/accounts/:accountId', {
        templateUrl: 'static/app/components/accounts/accountsViews/accounts-detail.html',
        controller: 'AccountDetailCtrl'
      }).
      otherwise({
        redirectTo: '/accounts'
      });
  }]);
