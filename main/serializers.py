# coding=utf-8
from rest_framework import serializers

from main.models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'iban')
