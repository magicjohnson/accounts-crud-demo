# coding=utf-8
from django.conf.urls import include, url
from rest_framework import routers

from main.views import AccountViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
