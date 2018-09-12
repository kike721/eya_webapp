# -*- coding: utf-8 -*-
from django.conf.urls import url
from store.views import add_item_cart, list_items

urlpatterns = [
    url(r'^agregar/(?P<pk>[0-9]+)/$', add_item_cart, name='add-item-cart' ),
    url(r'^lista/$', list_items, name='list-items' ),
]