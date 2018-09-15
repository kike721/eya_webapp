# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from products.models import Product
from store.forms import OrderForm, CartForm, DetailCartFormSet
from store.models import Cart, DetailCart, DetailOrder, Order
from utils.email import email_investor_confirmation


def add_detail_cart(request):
    if request.POST:
        id_cart = request.POST['cart']
        cart = Cart.objects.get(pk=id_cart)
        id_product = request.POST['product']
        product = Product.objects.get(pk=id_product)
        quantity = request.POST['quantity']
        if cart.details.filter(product=product):
            detail = cart.details.filter(product=product).first()
            detail.quantity += int(quantity)
            detail.save()
        else:
            detail = DetailCart.objects.create(cart=cart,product=product,quantity=quantity)
        return HttpResponseRedirect(reverse('cart', kwargs={'pk': id_cart}))
    return HttpResponseRedirect(reverse('home'))


def update_cart(request, pk):
    cart = Cart.objects.get(pk=pk)
    if request.POST:
        data = []
        for detail in cart.details.all():
            data.append(
                {'id':detail.pk, 'quantity': request.POST['{}-quantity'.format(detail.pk)]})
        for d in data:
            detail = DetailCart.objects.get(pk=d['id'])
            if '{}-delete'.format(d['id']) in request.POST:
                detail.delete()
            else:
                detail.quantity = d['quantity']
                detail.save()
        if 'orden' in request.POST:
            order = Order.objects.create(customer=cart.customer)
            for detail in cart.details.all():
                detailO = DetailOrder.objects.create(
                    order=order,product=detail.product, quantity=detail.quantity)
                detail.delete()
    return render(
        request, 'store/list_items.html', {'cart': cart, 'pk': pk})
