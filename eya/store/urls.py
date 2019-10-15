# -*- coding: utf-8 -*-
from django.conf.urls import url
from store.views import (
	add_detail_cart, history, update_cart, update_quotation,
	add_cart, get_cart, order_pdf, quotation_pdf, quotation_csv)

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', update_cart, name='cart' ),
    url(r'^agregar/$', add_detail_cart, name='add-detail-cart'),
    url(r'^historial/$', history, name='history'),
    url(r'^cotizacion/(?P<pk>[0-9]+)/$', update_quotation, name='update_quotation'),
    url(r'^add/$', add_cart, name='add-cart'),
    url(r'^get/$', get_cart, name='get-cart'),
    url(r'^order/(?P<pk>[0-9]+)/pdf$', order_pdf, name='order-pdf'),
    url(r'^cotizacion/(?P<pk>[0-9]+)/csv$', quotation_csv, name='quotation-csv'),
    url(r'^quotation/(?P<pk>[0-9]+)/pdf$', quotation_pdf, name='quotation-pdf'),
]