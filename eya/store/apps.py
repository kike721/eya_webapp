# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'
    verbose_name = 'Ordenes de compra'

    def ready(self):
        import store.signals # noqa
