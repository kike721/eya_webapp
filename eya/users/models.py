# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.db import models
from django.contrib.auth.models import Group, User, Permission
from django.urls import reverse
from django.utils import timezone

from smart_selects.db_fields import ChainedForeignKey

from utils.models import BaseModel, StateMx, MunicipalityMx, LocalityMx


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='customer')
    code = models.CharField(
        verbose_name=u'Código', max_length=10, blank=True, null=True, unique=True)
    name = models.CharField(verbose_name='Nombre completo', max_length=255)
    rfc = models.CharField(verbose_name='RFC', max_length=15)
    # Dirección facturación
    street = models.CharField(verbose_name='Calle', max_length=255, blank=True)
    zip_code = models.CharField(verbose_name=u'Código postal', max_length=5, blank=True)
    state = models.ForeignKey(StateMx, verbose_name='Estado')
    city = models.CharField(verbose_name='Ciudad', max_length=255, blank=True)
    # Contacto
    phone = models.CharField(verbose_name=u'Teléfono 1', max_length=10)
    phone_2 = models.CharField(verbose_name=u'Teléfono 2', max_length=10, null=True, blank=True)
    fax = models.CharField(verbose_name=u'Teléfono 2', max_length=10, null=True, blank=True)
    mobile = models.CharField(verbose_name=u'Celular', max_length=10, null=True, blank=True)
    contact = models.CharField(verbose_name=u'Persona de contacto', max_length=255, null=True, blank=True)
    active = models.BooleanField(verbose_name='¿Es activo?', default=0)

    
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


class Manager(BaseModel):
    NONE = ''
    SUPERADMIN = 'SUPERADMIN'
    TRADER = 'TRADER'
    PROVIDER = 'PROVIDER'
    BILLING = 'BILLING'

    USERS_TYPES_CHOICES = (
        (NONE, u'-------'),
        (SUPERADMIN, u'Super usuario'),
        (TRADER, u'Cotizador'),
        (PROVIDER, u'Surtidor'),
        (BILLING, u'Facturador'),
    )

    user = models.OneToOneField(
        User, related_name='manager', blank=True,
        on_delete=models.CASCADE, verbose_name='Usuario')

    type = models.CharField(max_length=10, choices=USERS_TYPES_CHOICES,
                            default=NONE, verbose_name='Tipo')

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = 'Administradores'

    def __unicode__(self):
        return "{} {} ({})".format(
            self.user.first_name,
            self.user.last_name,
            self.user.email,
        )

    def save(self, *args, **kwargs):
        if self.type == 'SUPERADMIN':
            group = Group.objects.get(name='Super Admin')
        elif self.type == 'TRADER':
            group = Group.objects.get(name='Trader')
        elif self.type == 'PROVIDER':
            group = Group.objects.get(name='Provider')
        elif self.type == 'BILLING':
            group = Group.objects.get(name='Billing')
        self.user.groups.clear()
        if self.type != Manager.NONE:
            self.user.groups.add(group)
        super(Manager, self).save(*args, **kwargs)
