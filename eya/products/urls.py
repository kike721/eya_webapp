# -*- coding: utf-8 -*-
from django.conf.urls import url
from products.views import (
	DetailProduct, IndexProducts, IndexNewProducts, IndexBestSellerProducts,
	IndexProductsResults)

urlpatterns = [
    url(r'^lista/', IndexProducts.as_view(), name='products-index'),
    url(r'^nuevos/', IndexNewProducts.as_view(), name='products-index-news'),
    url(r'^mas-vendidos/', IndexBestSellerProducts.as_view(),
    	name='products-index-best-seller'),
    url(r'^resultados/', IndexProductsResults.as_view(), name='products-index-results'),
    url(r'^(?P<pk>[0-9]+)/$', DetailProduct.as_view(), name='product-detail' ),
]

