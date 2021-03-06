# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from smart_selects.db_fields import ChainedForeignKey

from utils.models import StateMx, MunicipalityMx, LocalityMx


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='customer')
    code = models.CharField(
        verbose_name=u'Código', max_length=10, blank=True, null=True, unique=True)
    name = models.CharField(verbose_name='Nombre completo', max_length=255)
    rfc = models.CharField(verbose_name='RFC', max_length=15, blank=True)
    balance = models.DecimalField(verbose_name='Saldo', max_digits=10, decimal_places=2, default=0)
    name_foreign = models.CharField(verbose_name='Nombre extranjero', max_length=255, blank=True, null=True)
    # Dirección facturación
    street = models.CharField(verbose_name='Calle', max_length=255, blank=True)
    zip_code = models.CharField(verbose_name=u'Código postal', max_length=5, blank=True)
    state = models.ForeignKey(StateMx, verbose_name='Estado', null=True)
    city = models.CharField(verbose_name='Ciudad', max_length=255, blank=True)
    # Contacto
    phone = models.CharField(verbose_name=u'Teléfono 1', max_length=15, blank=True)
    phone_2 = models.CharField(verbose_name=u'Teléfono 2', max_length=15, null=True, blank=True)
    fax = models.CharField(verbose_name=u'Teléfono 2', max_length=15, null=True, blank=True)
    mobile = models.CharField(verbose_name=u'Celular', max_length=15, null=True, blank=True)
    contact = models.CharField(verbose_name=u'Persona de contacto', max_length=255, null=True, blank=True)
    active = models.BooleanField(verbose_name='¿Es activo?', default=0)
    # Balance
    code_employee = models.IntegerField(verbose_name='Codigo de empleado de venta', null=True)
    code_conditions_payment = models.IntegerField(verbose_name='Codigo condiciones de pago', null=True)
    limit_credit = models.DecimalField(verbose_name='Limite de crédito', max_digits=10, decimal_places=2, default=0)
    limit_debt = models.DecimalField(verbose_name='Limite de deuda',max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def get_absolute_url(self):
        return reverse('customer-request-register')

    @property
    def get_name(self):
        return '{}'.format(self.name)

    @property
    def address(self):
        return '{} {} {} {}'.format(self.street, self.city, self.state, self.zip_code)

    def __unicode__(self):
        return '{}'.format(self.get_name)


class Seller(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='seller', blank=True)
    name = models.CharField(verbose_name='Nombre completo', max_length=255)
    rfc = models.CharField(verbose_name='RFC', max_length=15, blank=True)
    address = models.CharField(verbose_name='Direccion', max_length=255, blank=True)
    phone = models.CharField(verbose_name=u'Teléfono', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __unicode__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        group = Group.objects.get(name='Seller')
        self.user.is_staff = True
        self.user.groups.clear()
        self.user.groups.add(group)
        self.user.save()
        super(Seller, self).save(*args, **kwargs)


class UserToken(models.Model):
    """Save token sended by email."""

    token = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    signup_date = models.DateTimeField(auto_now=True)
    is_reset = models.BooleanField(default=False)

    def has_expired(self):
        return (timezone.now() - self.signup_date) > timedelta(days=7)

    class Meta:
        unique_together = ('token', 'email')
