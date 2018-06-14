# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

from products.models import Product

# Create your views here.
def add_item_cart(request, pk):
	product = Product.objects.get(pk=pk)
	if request.session.has_key('products'):
		products = request.session['products']
		i = 0
		quantity = 0
		for prod in products:
			if prod['pk'] == product.pk:
				quantity = prod['quantity'] + 1
				break
			i += 1
		if quantity > 0:
			products[i]['quantity'] = quantity
		else:
			products.append({
				'pk': product.pk,
				'code': product.code_eyamex,
				'descr': product.description,
				'quantity': 1
			})
		request.session['products'] = products
	else:
		request.session['products'] = [
			{'pk': product.pk, 'code': product.code_eyamex, 'descr': product.description, 'quantity': 1}
		]
	print request.session['products']
	print 'session'
	# del request.session['products']
	return redirect('list-items')

def list_items(request):
	products = dict()
	if request.session.has_key('products'):
		products = request.session['products']
	print products
	return render(request, 'store/list_items.html', {'products': products})