# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from users.forms import CustomerForm, SellerForm
from users.models import Customer, Seller


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):

    form = CustomerForm


class SellerAdmin(admin.ModelAdmin):

    form = SellerForm


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
