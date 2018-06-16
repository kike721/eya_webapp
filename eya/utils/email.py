# -*- coding: utf-8 -*-
"""Emails."""
from __future__ import unicode_literals

import logging

from django.conf import settings
from django.core import mail
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import date as _date
from django.template.loader import render_to_string


logger = logging.getLogger('flowup')


def generate_send_email(to, subject, template, bcc=None):

    try:
        msg = mail.EmailMessage(
            subject,
            template,
            settings.DEFAULT_FROM_EMAIL,
            to,
            bcc,
            reply_to=[settings.EMAIL_REV_COPY],
        )
        msg.content_subtype = "html"

    except Exception as ex:
        print 'Error generate_send_email {}'.format(ex)
        return None

    return msg


def handle_send_email(emails):
    try:
        connection = mail.get_connection()
        connection.open()

        connection.send_messages(emails)
        connection.close()
    except Exception as ex:
        print 'Error handle_send_email {}'.format(ex)
        return False

    return True

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