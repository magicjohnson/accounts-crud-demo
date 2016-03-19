# coding=utf-8
import string

from django.core.exceptions import ValidationError
from django.core.validators import _lazy_re_compile
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class IbanValidator(object):
    IBAN_REGEX = _lazy_re_compile(r'^[A-Z0-9]{0,34}$')
    LETTER_MAP = tuple(zip(string.ascii_uppercase, range(10, 35)))
    message = _('IBAN is not valid')

    def __init__(self, message=None):
        if message is not None:
            self.message = message
        self.letter_map = dict(self.LETTER_MAP)

    def __call__(self, value):
        if not value or not self.IBAN_REGEX.match(value):
            raise ValidationError(self.message)

        iban = self._move_first_4_chars_to_the_end(value)
        number = self._get_iban_number(iban)

        if not self._is_mod_97_valid(number):
            raise ValidationError(self.message)

    def _get_iban_number(self, value):
        return int(self._get_iban_number_as_str(value))

    def _get_iban_number_as_str(self, value):
        return ''.join(
            [self._get_translated_number_as_str(s) for s in value]
        )

    def _get_translated_number_as_str(self, symbol):
        return str(self.letter_map.get(symbol, symbol))

    @staticmethod
    def _move_first_4_chars_to_the_end(value):
        return value[4:] + value[:4]

    @staticmethod
    def _is_mod_97_valid(number):
        return number % 97 == 1
