# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from store.models import Order

class OrderForm(forms.Form):
	name = forms.CharField(label=u"Nombre/Razón Social", max_length=255, required=True)
	address = forms.CharField(label=u"Dirección", max_length=255, required=True)
	phone = forms.CharField(label=u"Teléfono", max_length=10, required=True)

	def save(self):
		data = self.cleaned_data
		obj = Order.objects.create(
			name=data['name'],
			address=data['address'],
			phone=data['phone'])
		return obj