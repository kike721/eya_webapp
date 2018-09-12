# -*- coding: utf-8 -*-
"""Emails."""
from __future__ import unicode_literals

import logging

from utils.email import generate_send_email, handle_send_email
from django.template.loader import render_to_string

logger = logging.getLogger('eya')

def email_investor_confirmation(order):
    """Send Order Data Email."""
    template = render_to_string(
    	'emails/send_data_order.html',
    	{'order': order, 'details': order.details.all()})
    email = generate_send_email(
        ['jose.enrique.duran.garcia@gmail.com'],
        "Orden #{}".format(order.pk),
        template)

    return handle_send_email([email])