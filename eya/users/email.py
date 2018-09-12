# -*- coding: utf-8 -*-
"""Emails."""
from __future__ import unicode_literals

import logging

from django.conf import settings
from django.template.loader import render_to_string

from utils.email import generate_send_email, handle_send_email

logger = logging.getLogger('eya')

def register_confirm_email(token, customer):
    """Send Order Data Email."""
    print settings
    domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
    template = render_to_string(
    	'mailings/registro_confirmado.html',
    	{'customer': customer, 'domain': domain, 'token': token})
    email = generate_send_email(
        [customer.user.email],
        "Confirmar cuenta",
        template)

    return handle_send_email([email])