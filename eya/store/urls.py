# -*- coding: utf-8 -*-
from django.conf.urls import url
from store.views import add_detail_cart, history, update_cart, update_quotation, add_cart

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', update_cart, name='cart' ),
    url(r'^agregar/$', add_detail_cart, name='add-detail-cart'),
    url(r'^historial/$', history, name='history'),
    url(r'^cotizacion/(?P<pk>[0-9]+)/$', update_quotation, name='update_quotation'),
    url(r'^add/$', add_cart, name='add-cart'),
]