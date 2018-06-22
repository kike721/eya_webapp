# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='customer', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __unicode__(self):
        return '{}'.format(self.user)


class Seller(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='seller', blank=True)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __unicode__(self):
        return '{}'.format(self.user)
