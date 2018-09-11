# -*- coding: utf-8 -*-
from django.conf.urls import url
from products.views import IndexProducts, IndexNewProducts, IndexBestSellerProducts

urlpatterns = [
    url(r'^lista/', IndexProducts.as_view(), name='products-index'),
    url(r'^nuevos/', IndexNewProducts.as_view(), name='products-index-news'),
    url(r'^mas-vendidos/', IndexBestSellerProducts.as_view(), name='products-index-best-seller'),
]
