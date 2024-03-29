# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-15 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20181115_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Saldo'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='limit_credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Limite de cr\xe9dito'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='limit_debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Limite de deuda'),
        ),
    ]
