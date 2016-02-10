"""
Tests for validation_utils.py
"""

from ddt import ddt, data

from django.core.exceptions import ValidationError
from django.test import TestCase
from util.validation_utils import validate_email


@ddt
class ValidationUtilsTest(TestCase):
    """
    Tests for validate_email

    Reuses test cases from Django 1.4.21 validator tests;
    adds test cases for new TLDs.
    """

    @data(
        'email@here.com',
        'weirder-email@here.and.there.com',
        'email@[127.0.0.1]',
        # Quoted-string format
        '"\\\011"@here.com',
        # New TLDs (not supported by Django 1.4.21)
        'email@here.solutions',
        'weirder-email@here.and.there.academy',
        '"\\\011"@here.boutique',
    )
    def test_validate_email_valid(self, email):
        self.assertIsNone(validate_email(email))

    @data(
        None,
        '',
        'abc',
        'a @x.cz',
        'something@@somewhere.com',
        'email@127.0.0.1',
        # Quoted-string format (CR not allowed)
        '"\\\012"@here.com'
        # Trailing newlines in username or domain not allowed
        'a@b.com\n',
        'a\n@b.com',
        '"test@test"\n@example.com',
        'a@[127.0.0.1]\n',
        # New TLDs (not supported by Django 1.4.21)
        'something@@somewhere.camera',
        '"\\\012"@here.careers'
        'a@b.bargains\n',
        'a\n@b.builders',
        '"test@test"\n@example.clothing',
    )
    def test_validate_email_invalid(self, email):
        self.assertRaises(ValidationError, validate_email, email)
