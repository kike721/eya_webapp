# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from products.models import Product
from utils.models import BaseModel

# Create your models here.

class Order(BaseModel):
	name = models.CharField(verbose_name=u'Nombre/Razón Social', max_length=255)
	address = models.CharField(verbose_name=u'Dirección', max_length=255)
	phone = models.CharField(verbose_name=u'Teléfono', max_length=255)

	class Meta:
		verbose_name = u'Orden de compra'
		verbose_name_plural = u'Ordenes de compra'


	def __unicode_(self):
		return u'Order-{} {}'.format(self.pk, self.name)


class DetailOrder(BaseModel):
	order = models.ForeignKey(Order, verbose_name=u'Orden')
	product = models.ForeignKey(Product, verbose_name=u'Producto')

	class Meta:
		verbose_name = u'Detalle de orden'
		verbose_name_plural = u'Detalles de orden'

	def __unicode_(self):
		return u'Order-{} {}'.format(self.pk, self.product)