# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-16 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180908_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'PENDIENTE'), ('F', 'FINALIZADA')], default='P', max_length=3, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='users.Customer', verbose_name='Cliente'),
        ),
    ]
