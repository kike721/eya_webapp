# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from smart_selects.db_fields import ChainedForeignKey

from utils.models import StateMx, MunicipalityMx, LocalityMx


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='customer')
    name = models.CharField(verbose_name='Nombre completo', max_length=255)
    rfc = models.CharField(verbose_name='RFC', max_length=15)
    address = models.CharField(verbose_name='Direccion', max_length=255)
    phone = models.CharField(verbose_name=u'Teléfono', max_length=255)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def get_absolute_url(self):
        return reverse('customer-request-register')

    @property
    def get_name(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return '{}'.format(self.get_name)


class Seller(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='seller', blank=True)
    name = models.CharField(verbose_name='Nombre completo', max_length=255)
    rfc = models.CharField(verbose_name='RFC', max_length=15)
    address = models.CharField(verbose_name='Direccion', max_length=255)
    phone = models.CharField(verbose_name=u'Teléfono', max_length=255)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    @property
    def get_name(self):
        return '{} {} {}'.format(
            self.first_name, self.last_name, self.second_last_name)

    def __unicode__(self):
        return '{}'.format(self.get_name)
