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
        {'products': products, 'seccion': 'list-order', 'form': form})


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
            print detail
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
        request, 'store/cart.html', {'cart': cart, 'pk': pk})
