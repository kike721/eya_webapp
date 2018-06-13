# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView

from products.models import Product


# Create your views here.
class IndexProducts(ListView):

    model = Product
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(IndexProducts, self).get_context_data(**kwargs)
        obj = self.object_list[0]
        print obj.image
        return context