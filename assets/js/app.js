var accountApp = angular.module(
    'accountApp', ['ui.router', 'ngResource', 'accountApp.controllers', 'accountApp.services']
);

accountApp.config(function ($stateProvider) {
    $stateProvider.state('account-list', {
        url: '/accounts/',
        templateUrl: '/static/accountApp/partials/account-list.html',
        controller: 'AccountListController'
    }).state('account-add', {
        url: '/accounts/add/',
        templateUrl: '/static/accountApp/partials/account-add.html',
        controller: 'AccountAddController'
    }).state('account-detail', {
        url: '/accounts/:id/',
        templateUrl: '/static/accountApp/partials/account-detail.html',
        controller: 'AccountDetailController'
    }).state('account-edit', {
        url: '/accounts/:id/edit/',
        templateUrl: '/static/accountApp/partials/account-edit.html',
        controller: 'AccountEditController'
    })
}).run(function ($state) {
    $state.go('account-list');
});

accountApp.config(function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
);

accountApp.config(function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});
