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

    def get_products(self):
        products = list()
        for detail in self.details.all():
            products.append(detail.product)
        return products

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

    PENDING = 'P'
    FINISHED = 'F'

    STATUS_ORDER = (
        (PENDING,'PENDIENTE'),
        (FINISHED,'FINALIZADA'),
    )

    customer = models.ForeignKey(
        Customer, verbose_name='Cliente', related_name='orders')
    seller = models.ForeignKey(
        Seller, verbose_name='Vendedor', related_name='s_orders', null=True,
        blank=True)
    status = models.CharField(verbose_name='Estatus', max_length=3, choices=STATUS_ORDER, default=PENDING)

    class Meta:
        verbose_name = u'Orden de compra'
        verbose_name_plural = u'Ordenes de compra'


    def __unicode__(self):
        return u'Order-{} {}'.format(self.pk, self.customer)

    def total(self):
        total = Decimal(0.0)
        for detail in self.details.all():
            total += detail.price
        return total


class DetailOrder(BaseModel):
    order = models.ForeignKey(
        Order, verbose_name=u'Orden', related_name='details')
    product = models.ForeignKey(Product, verbose_name=u'Producto')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    price = models.DecimalField(verbose_name='Precio', max_digits=10, decimal_places=2, default=0)
    discount = models.PositiveIntegerField(verbose_name='Descuento', default=0)

    class Meta:
        verbose_name = u'Detalle de orden'
        verbose_name_plural = u'Detalles de orden'

    def __unicode_(self):
        return u'Order-{} {} {}'.format(self.pk, self.quantity, self.product)
