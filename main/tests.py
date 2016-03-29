# coding=utf-8
from django.core.exceptions import ValidationError
from django.test import TestCase

from main.validators import IbanValidator


class IBANValidatorTest(TestCase):
    def _assert_iban_is_not_valid(self, value):
        with self.assertRaises(ValidationError):
            IbanValidator()(value)

    def _assert_iban_is_valid(self, value):
        IbanValidator()(value)

    def test_blank_iban(self):
        self._assert_iban_is_not_valid('')

    def test_iban_length_is_not_correct(self):
        self._assert_iban_is_not_valid('X' * 35)

    def test_iban_contains_illegals_chars(self):
        self._assert_iban_is_not_valid('=')

    def test_iban_mod_is_not_1(self):
        self._assert_iban_is_not_valid('DE44500105175407324932')
        self._assert_iban_is_not_valid('231011Z0000000013701000194410Z21')

    def test_valid_iban(self):
        self._assert_iban_is_valid('DE44500105175407324931')
        self._assert_iban_is_valid('GR1601101250000000012300695')
        self._assert_iban_is_valid('GB29NWBK60161331926819')
        self._assert_iban_is_valid('SA0380000000608010167519')
        self._assert_iban_is_valid('CH9300762011623852957')

    def test_message_is_customizable(self):
        try:
            IbanValidator(message='My message')('')
            self.fail()
        except ValidationError as e:
            self.assertEqual(e.message, 'My message')
