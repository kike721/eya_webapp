# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from products.models import Product
from users.models import Customer


# Home View
class IndexProducts(ListView):

    model = Product
    paginate_by = 12

    def get_queryset(self):
        queryset = super(IndexProducts, self).get_queryset().order_by('code_eyamex')
        queryset = queryset.filter(spent=False, is_new=False, best_seller=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexProducts, self).get_context_data(**kwargs)
        domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
        context['news'] = Product.objects.filter(spent=False, is_new=True).order_by('code_eyamex')[:20]
        context['best_seller'] = Product.objects.filter(spent=False, best_seller=True).order_by('code_eyamex')[:20]
        context['customers'] = Customer.objects.filter(active=True)
        context['current_page'] = int(self.request.GET.get('page', 1))
        context['domain'] = domain
        return context

# Results search View
class IndexProductsResults(ListView):

    model = Product
    paginate_by = 12
    template_name = 'products/results.html'

    def get_queryset(self):
        queryset = super(IndexProductsResults, self).get_queryset()
        queryset = queryset.filter(spent=False).order_by('code_eyamex')
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
        context['current_page'] = int(self.request.GET.get('page', 1))
        context['domain'] = domain
        return context

# List new products
class IndexNewProducts(ListView):

    model = Product
    paginate_by = 12
    template_name = 'products/news_list.html'

    def get_queryset(self):
        queryset = super(IndexNewProducts, self).get_queryset()
        queryset = queryset.filter(spent=False, is_new=True).order_by('code_eyamex')
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
        context['current_page'] = int(self.request.GET.get('page', 1))
        return context

# List bestSeller products
class IndexBestSellerProducts(ListView):

    model = Product
    paginate_by = 12
    template_name = 'products/best_seller_list.html'

    def get_queryset(self):
        queryset = super(IndexBestSellerProducts, self).get_queryset()
        queryset = queryset.filter(spent=False, best_seller=True).order_by('code_eyamex')
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
        context['current_page'] = int(self.request.GET.get('page', 1))
        return context


# Detail View products
class DetailProduct(DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProduct, self).get_context_data(**kwargs)
        obj = super(DetailProduct, self).get_object()
        domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
        context['customers'] = Customer.objects.filter(active=True)
        context['domain'] = domain
        context['products_related'] = obj.get_products_related()
        return context