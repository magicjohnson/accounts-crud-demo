angular.module('accountApp.services', []).factory('Account', function($resource) {
  return $resource('/api/v1/accounts/:id/', { id: '@id' }, {
    update: {
      method: 'PUT'
    }
  });
});
