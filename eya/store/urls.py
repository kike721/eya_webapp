# -*- coding: utf-8 -*-
from django.conf.urls import url
from store.views import add_detail_cart, history, update_cart

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', update_cart, name='cart' ),
    url(r'^agregar/$', add_detail_cart, name='add-detail-cart'),
    url(r'^historial/$', history, name='history'),
]