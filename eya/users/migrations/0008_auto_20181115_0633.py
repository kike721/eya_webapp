# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-15 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181104_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Saldo'),
        ),
        migrations.AddField(
            model_name='customer',
            name='code_conditions_payment',
            field=models.IntegerField(null=True, verbose_name='Codigo condiciones de pago'),
        ),
        migrations.AddField(
            model_name='customer',
            name='code_employee',
            field=models.IntegerField(null=True, verbose_name='Codigo de empleado de venta'),
        ),
        migrations.AddField(
            model_name='customer',
            name='limit_credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Limite de cr\xe9dito'),
        ),
        migrations.AddField(
            model_name='customer',
            name='limit_debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Limite de deuda'),
        ),
        migrations.AddField(
            model_name='customer',
            name='name_foreign',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre extranjero'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='rfc',
            field=models.CharField(blank=True, max_length=15, verbose_name='RFC'),
        ),
    ]