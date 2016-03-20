var controllers = angular.module('accountApp.controllers', []);


controllers.controller('BaseController', function ($http, $scope, $state, $stateParams, Account) {
    function handleErrors(errorResponse) {
        if (errorResponse.status === 404) {
            $scope.is404 = true;
        }
        if (errorResponse.status === 400) {
            $scope.$errors = errorResponse.data;
        }
    }

    function redirectToList() {
        $state.go('account-list');
    }

    $scope.$watch(
        function () {
            return $http.pendingRequests.length;
        }, function () {
            $scope.loading = $http.pendingRequests.length > 0;
        }
    );

    $scope.addAccount = function () {
        $scope.account.$save(redirectToList, handleErrors);
    };

    $scope.getAccount = function () {
        return Account.get({id: $stateParams.id}, null, handleErrors);
    };

    $scope.deleteAccount = function (account) {
        account.$delete(function () {
            $scope.accounts = Account.query();
        });
    };

    $scope.updateAccount = function () {
        $scope.account.$update(redirectToList, handleErrors);
    };
})
;

controllers.controller('AccountListController', function ($scope, $controller, $window, Account) {
    angular.extend(this, $controller('BaseController', {$scope: $scope}));
    $scope.accounts = Account.query();
});

controllers.controller('AccountAddController', function ($scope, $controller, $stateParams, Account) {
    angular.extend(this, $controller('BaseController', {$scope: $scope}));
    $scope.account = new Account();
});

controllers.controller('AccountDetailController', function ($scope, $controller) {
    angular.extend(this, $controller('BaseController', {$scope: $scope}));
    $scope.account = $scope.getAccount();
});

controllers.controller('AccountEditController', function ($scope, $controller) {
    angular.extend(this, $controller('AccountDetailController', {$scope: $scope}));
});


