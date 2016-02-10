import re

from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _

# This is a modified version of the regexp that Django 1.4.21 uses to validate email addresses.
# It matches email addresses with newer TLDs.
# Modifications are based on "domain_regex" from Django 1.8.9 (which also matches email addresses with newer TLDs).
email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    # quoted-string, see also http://tools.ietf.org/html/rfc2822#section-3.2.5
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'
    r')@((?:[A-Z0-9](?:[A-Z0-9-]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z)'  # domain
    r'|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]\Z', re.IGNORECASE)  # literal form, ipv4 address (SMTP 4.1.3)

validate_email = EmailValidator(email_re, _(u'Enter a valid e-mail address.'), 'invalid')
