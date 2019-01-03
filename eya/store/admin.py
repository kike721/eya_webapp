# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from store.models import DetailOrder, Order
from .email import send_quotation_customer


class DetailOrderInline(admin.TabularInline):

    model = DetailOrder
    readonly_fields = ('product', 'quantity')
    extra = 0
    can_delete = False


class OrderAdmin(admin.ModelAdmin):

    list_display = ('customer', 'date')
    fields = ('customer', 'date', 'status')
    readonly_fields = ('customer', 'date')
    inlines = [DetailOrderInline]
    search_fields = ('customer__name',)
    list_filter = ('created', )

    def response_change(self, request, obj):
        if obj.old_status == Order.PENDING and obj.status == Order.QUOTATION:
            send_quotation_customer(obj)
        return super(OrderAdmin, self).response_change(request, obj)

    def date(self, obj):
        return obj.created.strftime('%d-%m-%Y')

    date.short_description = 'Fecha'

admin.site.register(Order, OrderAdmin)
