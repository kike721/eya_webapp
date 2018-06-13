# -*- coding: utf-8 -*-
from django.conf.urls import url
from products.views import IndexProducts

urlpatterns = [
    url(r'^index/', IndexProducts.as_view(), name='products-index' ),
]
