# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView

from products.models import Product


# Create your views here.
class IndexProducts(ListView):

    model = Product
    paginate_by = 12

    def get_queryset(self):
    	queryset = super(IndexProducts, self).get_queryset()
    	if self.request.GET.has_key('q'):
    		q = self.request.GET['q']
    		queryset = queryset.filter(meta_description__icontains=q)
    	return queryset