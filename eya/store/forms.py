# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from store.models import Cart, DetailCart, Order, DetailOrder

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


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        exclude = ['customer']


DetailCartFormSet = forms.inlineformset_factory(
    Cart, DetailCart, fields=('quantity',), extra=0)

QuotationFormset = forms.inlineformset_factory(
    Order, DetailOrder, fields=('quantity', 'status',), extra=0, can_delete=False)