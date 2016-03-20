# coding=utf-8
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet

from main.models import Account
from main.serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class IndexView(TemplateView):
    template_name = 'main/index.html'
