# -*- coding: utf-8 -*-
from django.conf.urls import url
from products.views import IndexProducts, IndexNewProducts, IndexBestSellerProducts

urlpatterns = [
    url(r'^index/', IndexProducts.as_view(), name='products-index'),
    url(r'^news/', IndexNewProducts.as_view(), name='products-index-news'),
    url(r'^best-seller/', IndexBestSellerProducts.as_view(), name='products-index-best-seller'),
]
