var accountApp = angular.module(
    'accountApp', ['ui.router', 'ngResource', 'accountApp.controllers', 'accountApp.services']
);

accountApp.config(function ($stateProvider) {
    $stateProvider.state('account-list', {
        url: '/accounts/',
        templateUrl: '/static/accountApp/partials/account-list.html',
        controller: 'AccountListController'
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
