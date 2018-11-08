# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render
from django.views.generic.list import ListView

from products.models import Product
from users.models import Customer


# Create your views here.
class IndexProducts(ListView):

    model = Product
    paginate_by = 12

    def get_queryset(self):
    	queryset = super(IndexProducts, self).get_queryset()
    	queryset = queryset.filter(spent=False, is_new=False, best_seller=False)
    	return queryset

    def get_context_data(self, **kwargs):
    	context = super(IndexProducts, self).get_context_data(**kwargs)
        domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
    	context['news'] = Product.objects.filter(spent=False, is_new=True)[:20]
    	context['best_seller'] = Product.objects.filter(spent=False, best_seller=True)[:20]
        context['customers'] = Customer.objects.filter(active=True)
        context['domain'] = domain
    	return context

class IndexProductsResults(ListView):

    model = Product
    paginate_by = 12
    template_name = 'products/results.html'

    def get_queryset(self):
        queryset = super(IndexProductsResults, self).get_queryset()
        queryset = queryset.filter(spent=False)
        q = ''
        if self.request.GET.has_key('q'):
            q = self.request.GET['q']
            queryset = queryset.filter(meta_description__icontains=q)
        self.q = q
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexProductsResults, self).get_context_data(**kwargs)
        domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
        context['q'] = self.q
        context['customers'] = Customer.objects.filter(active=True)
        context['domain'] = domain
        return context


class IndexNewProducts(ListView):

    model = Product
    paginate_by = 12
    template_name = 'products/news_list.html'

    def get_queryset(self):
    	queryset = super(IndexNewProducts, self).get_queryset()
    	queryset = queryset.filter(spent=False, is_new=True)
    	q = ''
    	if self.request.GET.has_key('q'):
    		q = self.request.GET['q']
    		queryset = queryset.filter(meta_description__icontains=q)
    	self.q = q
    	return queryset

    def get_context_data(self, **kwargs):
    	context = super(IndexNewProducts, self).get_context_data(**kwargs)
        domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
    	context['q'] = self.q
        context['customers'] = Customer.objects.filter(active=True)
        context['domain'] = domain
    	return context


class IndexBestSellerProducts(ListView):

    model = Product
    paginate_by = 12
    template_name = 'products/best_seller_list.html'

    def get_queryset(self):
    	queryset = super(IndexBestSellerProducts, self).get_queryset()
    	queryset = queryset.filter(spent=False, best_seller=True)
    	q = ''
    	if self.request.GET.has_key('q'):
    		q = self.request.GET['q']
    		queryset = queryset.filter(meta_description__icontains=q)
    	self.q = q
    	return queryset

    def get_context_data(self, **kwargs):
    	context = super(IndexBestSellerProducts, self).get_context_data(**kwargs)
        domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
    	context['q'] = self.q
        context['customers'] = Customer.objects.filter(active=True)
        context['domain'] = domain
    	return context