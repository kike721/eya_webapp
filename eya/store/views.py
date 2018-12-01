# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from products.models import Product
from store.forms import OrderForm, CartForm, DetailCartFormSet, QuotationFormset
from store.models import Cart, DetailCart, DetailOrder, Order
from store.email import send_order_customer, send_order_eya
from utils.email import email_investor_confirmation
from users.models import Customer


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
    domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
    customer = cart.customer
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
            send_order_eya(order)
            send_order_customer(order)
            return HttpResponseRedirect(reverse('customer-profile', kwargs={'pk': cart.customer.pk}))
    return render(
        request, 'store/list_items.html', {'cart': cart, 'pk': pk, 'customer': customer, 'domain': domain})


def history(request):
    id_cart = request.session['cart_selected']
    cart = Cart.objects.get(pk=id_cart)
    customer = cart.customer
    domain = '{}{}'.format(settings.HTTP_PROTOCOL, settings.CURRENT_DOMAIN)
    orders = DetailOrder.objects.filter(order__customer=customer)
    products = list()
    for order in orders:
        if order.product not in products:
            products.append(order.product)
    history = []
    for product in products:
        data_history = DetailOrder.objects.filter(product=product, order__customer=customer).order_by('-created')
        history.append({'code': product.code_eyamex, 'history': data_history})
    return render(
        request, 'store/history.html', {'domain': domain, 'history': history, 'customer': customer })


def update_quotation(request, pk):
    order = Order.objects.get(pk=pk)
    if request.POST:
        form = QuotationFormset(request.POST, instance=order)
        with transaction.atomic():
            if form.is_valid():
                form.save()
    else:
        form = QuotationFormset(instance=order)
    return render(
        request,
        'store/update_quotation.html',
        {
            'form': form,
            'order': order,
        }
    )