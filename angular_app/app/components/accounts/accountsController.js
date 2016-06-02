'use strict';

/* Accounts Controllers */

var accountsControllers = angular.module('accountsControllers', []);

accountsControllers.controller('AccountListCtrl', ['$scope', 'Account',
  function($scope, Account) {
    $scope.accounts = Account.query();
    $scope.sortType = 'status';
    $scope.sortReverse = false;
    $scope.searchAccount = '';

    $scope.columns = ['account', 'id', 'status', 'active_campaigns', 'sponsored_jobs', 'account_balance', 'monthly_budget'];
  }]);

accountsControllers.controller('AccountDetailCtrl', ['$scope', '$routeParams',
  function($scope, $routeParams) {
    $scope.AccountId = $routeParams.accountId;
    $scope.account = {'name': 'Account 1', 'balance': 1000, 'email': 'pavan@simplyhired.com'};
  }]);


accountsControllers.controller('AccountCreateCtrl', ['$scope',
  function($scope) {
    $scope.create = 'asdfasdf';
  }]);
