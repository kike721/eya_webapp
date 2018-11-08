# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from store.models import DetailOrder,Order
from users.forms import CustomerAdminForm, SellerAdminForm, ManagerForm, ManagerAdminForm
from users.models import Customer, Seller, Manager


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

    form = SellerAdminForm


class ManagerAdmin(admin.ModelAdmin):
    model = Manager

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = ManagerForm
        elif request.user.manager.type=='SUPERADMIN':
            kwargs['form'] = ManagerForm
        else:
            kwargs['form'] = ManagerAdminForm
        return super(ManagerAdmin, self).get_form(request, obj, **kwargs)

    def get_queryset(self, request):
        qs = super(ManagerAdmin, self).get_queryset(request)
        if (request.user.is_superuser or (
                hasattr(request.user, 'manager') and
                request.user.manager.type == 'SUPERADMIN')):
            return qs
        return qs.exclude(type=Manager.SUPERADMIN)

# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Seller, SellerAdmin)
