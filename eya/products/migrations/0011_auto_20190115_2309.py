# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-16 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190112_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelproduct',
            name='family_product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='ModelProduct',
        ),
    ]