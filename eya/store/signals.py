# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .email import send_quotation_customer
from .models import Order


@receiver(pre_save, sender=Order)
def check_status_order(sender, instance, **kwargs):
    instance.old_status = None
    if instance.pk:
        obj = Order.objects.get(pk=instance.pk)
        instance.old_status = obj.status


@receiver(post_save, sender=Order)
def send_email_quotation(sender, instance, **kwargs):
    if (instance.old_status != instance.status) and (instance.status == Order.QUOTATION):
    	print 'Enviando cotización'
        send_quotation_customer(instance)
