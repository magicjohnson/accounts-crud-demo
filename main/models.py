from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from main.validators import IbanValidator


class Account(models.Model):
    first_name = models.CharField(max_length=512, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=512, verbose_name=_('Last Name'))
    iban = models.CharField(max_length=34, verbose_name=_('IBAN'), validators=[IbanValidator()])
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created by'))

    def __repr__(self):
        return "<Account: {0} {1}>".format(self.first_name, self.last_name)

