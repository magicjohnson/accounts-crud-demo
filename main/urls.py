# coding=utf-8
from django.conf.urls import include, url
from rest_framework import routers

from main.views import AccountViewSet, IndexView

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url('^$', IndexView.as_view(), name='index'),
]
