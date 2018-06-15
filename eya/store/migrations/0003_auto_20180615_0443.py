# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_detailorder_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='store.Order', verbose_name='Orden'),
        ),
    ]
