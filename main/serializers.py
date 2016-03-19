# coding=utf-8
from rest_framework import serializers

from main.models import Account


class NoUserException(Exception):
    pass


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('url', 'first_name', 'last_name', 'iban')

    def create(self, validated_data):
        try:
            validated_data['creator'] = self.context['request'].user
            return super().create(validated_data)
        except (KeyError, AttributeError):
            raise NoUserException()
