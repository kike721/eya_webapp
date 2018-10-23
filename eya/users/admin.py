# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from store.models import DetailOrder,Order
from users.forms import CustomerAdminForm, SellerForm
from users.models import Customer, Seller


class OrderDetailUserInline(NestedStackedInline):

    model = DetailOrder
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')


class OrderUserInline(NestedStackedInline):

    model = Order
    extra = 0
    exclude = ('seller',)
    inlines = [OrderDetailUserInline]
    readonly_fields = ('status',)


class CustomerAdmin(NestedModelAdmin):

    model = Customer
    form = CustomerAdminForm
    inlines = [OrderUserInline]


class SellerAdmin(admin.ModelAdmin):

    form = SellerForm


admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Seller, SellerAdmin)
