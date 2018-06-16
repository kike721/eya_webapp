# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from products.models import Product
from store.forms import OrderForm
from store.models import DetailOrder
from utils.email import email_investor_confirmation

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
	return redirect('list-items')

def list_items(request):
	products = dict()
	if request.session.has_key('products'):
		products = request.session['products']

	print products
	return render(request, 'store/list_items.html', {'products': products, 'seccion': 'list-order'})

	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save()
			for prod in products:
				product = Product.objects.get(pk=prod['pk'])
				detailOrder = DetailOrder.objects.create(
					order=order,
					product=product,
					quantity=prod['quantity'])
				email_investor_confirmation(order)
			del request.session['products']
			return HttpResponseRedirect(reverse('home'))
	return render(
		request,
		'store/list_items.html',
		{'products': products, 'form': form})

