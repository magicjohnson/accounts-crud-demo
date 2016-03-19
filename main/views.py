# coding=utf-8

from rest_framework.viewsets import ModelViewSet

from main.models import Account
from main.serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
