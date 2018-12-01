# -*- coding: utf-8 -*-
"""Emails."""
from __future__ import unicode_literals

import logging

from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
from utils.email import generate_send_email, handle_send_email

logger = logging.getLogger('eya')

def send_order_eya(order):
    """Send Order Data Email."""
    template = render_to_string(
    	'emails/send_data_order.html',
    	{'order': order, 'details': order.details.all()})
    email = generate_send_email(
        # ['cotizaciones@ensamblesyadornos.org', 'ensamblesyadornos2007mexico@gmail.com'],
        ['jose.enrique.duran.garcia@gmail.com', 'valeria.pjaimes@gmail.com'],
        "Orden #{}".format(order.pk),
        template)

    return handle_send_email([email])

def send_order_customer(order):
    """Send Order Data Email."""
    template = render_to_string(
    	'mailings/enviar_pedido.html',
    	{'order': order, 'details': order.details.all()})
    email = generate_send_email(
        [order.customer.user.email],
        "Orden #{}".format(order.pk),
        template)

    return handle_send_email([email])

def send_quotation_customer(order):
    """Send Order Data Email."""
    domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
    url = '{}{}'.format(domain, reverse('update_quotation', kwargs={'pk': order.pk}))
    template = render_to_string(
        'mailings/enviar_cotizacion.html',
        {'order': order, 'details': order.details.all(), 'url': url})
    email = generate_send_email(
        [order.customer.user.email],
        "Cotización de orden #{}".format(order.pk),
        template)

    return handle_send_email([email])