# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-08 22:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180622_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Nombre completo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=255, verbose_name='Tel\xe9fono'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='rfc',
            field=models.CharField(default='', max_length=15, verbose_name='RFC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Nombre completo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='phone',
            field=models.CharField(default='', max_length=255, verbose_name='Tel\xe9fono'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='rfc',
            field=models.CharField(default='', max_length=15, verbose_name='RFC'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
