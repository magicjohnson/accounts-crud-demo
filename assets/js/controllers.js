var controllers = angular.module('accountApp.controllers', []);


controllers.controller('BaseController', function ($http, $scope) {
    $scope.$watch(
        function () {
            return $http.pendingRequests.length;
        }, function () {
            $scope.loading = $http.pendingRequests.length > 0;
        }
    );
})
;

controllers.controller('AccountListController', function ($scope, $state, $controller, $window, Account) {
    angular.extend(this, $controller('BaseController', {$scope: $scope}));
    $scope.accounts = Account.query();
});


