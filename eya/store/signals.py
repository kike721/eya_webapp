# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .email import send_quotation_customer, send_supply_eya, send_supply_customer
from .models import DetailOrder,Order


@receiver(pre_save, sender=Order)
def check_status_order(sender, instance, **kwargs):
    instance.old_status = None
    if instance.pk:
        obj = Order.objects.get(pk=instance.pk)
        instance.old_status = obj.status


@receiver(post_save, sender=Order)
def send_email_quotation(sender, instance, **kwargs):
    if instance.status == Order.QUOTATION:
        if len(instance.details.filter(status=DetailOrder.PENDING)) == 0:
            instance.status = Order.SUPPLY
            instance.save()
            send_supply_eya(instance)
            send_supply_customer(instance)
