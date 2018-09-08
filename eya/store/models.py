# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from products.models import Product
from utils.models import BaseModel
from users.models import Customer, Seller


# Create your models here.
class Cart(BaseModel):
    customer = models.OneToOneField(
        Customer, verbose_name='Usuario', related_name='cart')

class DetailCart(models.Model):
    cart = models.ForeignKey(
        Cart, verbose_name='Detalle de carrito', related_name='details')
    product = models.ForeignKey(
        Product, verbose_name='Producto', related_name='cart_products')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')


class CartSeller(BaseModel):
    seller = models.OneToOneField(
        Seller, verbose_name='Vendedor', related_name='s_cart')


class DetailSellerCart(models.Model):
    cart = models.ForeignKey(
        CartSeller, verbose_name='Detalle de carrito',
        related_name='sc_details')
    product = models.ForeignKey(
        Product, verbose_name='Producto', related_name='cart_seller_products')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')


class Order(BaseModel):
    customer = models.ForeignKey(
        Customer, verbose_name='Usuario', related_name='orders')
    seller = models.ForeignKey(
        Seller, verbose_name='Vendedor', related_name='s_orders', null=True,
        blank=True)

    class Meta:
        verbose_name = u'Orden de compra'
        verbose_name_plural = u'Ordenes de compra'


    def __unicode_(self):
        return u'Order-{} {}'.format(self.pk, self.customer)


class DetailOrder(BaseModel):
    order = models.ForeignKey(
        Order, verbose_name=u'Orden', related_name='details')
    product = models.ForeignKey(Product, verbose_name=u'Producto')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')

    class Meta:
        verbose_name = u'Detalle de orden'
        verbose_name_plural = u'Detalles de orden'

    def __unicode_(self):
        return u'Order-{} {} {}'.format(self.pk, self.quantity, self.product)
