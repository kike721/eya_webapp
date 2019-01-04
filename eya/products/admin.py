# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse

from products.models import (Clasification, Color, Family, ModelProduct, Product, Type)


class ImageProductFilter(admin.SimpleListFilter):
    title = (u'Tiene imagen')

    parameter_name = 'image'

    def lookups(self, request, model_admin):
        return (
            ('CI', 'Con imagen'),
            ('SI', 'Sin imagen')
        )

    def queryset(self, request, queryset):
        ids = []
        if self.value() == 'CI':
            for q in queryset:
                if q.image:
                    ids.append(q.pk)
            return queryset.filter(id__in=ids)
        if self.value() == 'SI':
            for q in queryset:
                if not q.image:
                    ids.append(q.pk)
            return queryset.filter(id__in=ids)

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = (
        'code_eyamex', 'image', 'type', 'clasification', 'model',
        'code', 'color', 'description', 'is_new', 'best_seller', 'spent')
    list_display = ('code_eyamex', 'description', 'family')
    list_filter = (ImageProductFilter,)
    ordering = ('code_eyamex',)
    search_fields = ('code_eyamex', 'code', 'model__code', 'description')
    actions = ['export_csv']
    
    def family(self, obj):
        return obj.model.family_product
    family.short_description = 'Familia'

    def export_csv(modeladmin, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Proyectos.csv"'
        writer = csv.writer(response)
        writer.writerow(
            [ 'Total', queryset.count()]
        )
        writer.writerow(
            ['Codigo eyamex', 'Descripcion']
        )
        for product in queryset:
            writer.writerow(
                [product.code_eyamex, product.description.encode('utf-8')]
            )
        return response
    export_csv.short_description = 'Exportar a Csv'


class ModelProductAdmin(admin.ModelAdmin):
    model = ModelProduct
    fields = ('code', 'family_product')
    ordering = ('code',)
    list_display = ('code', 'family_product')
    search_fields = ('code',)


class ClasificationAdmin(admin.ModelAdmin):
    model = Clasification
    fields = ('name', 'display_name')
    list_display = ('name', 'display_name')
    ordering = ('name',)
    search_fields = ('name',)


class ColorAdmin(admin.ModelAdmin):
    model = Color
    fields = ('name', 'display_name')
    list_display = ('name', 'display_name')
    ordering = ('name',)
    search_fields = ('name',)


class ModelInlineAdmin(admin.TabularInline):
    model = ModelProduct
    readonly_fields = ('code',)
    can_delete = False


class FamilyAdmin(admin.ModelAdmin):
    model = Family
    fields = ('code',)
    ordering = ('code',)
    search_fields = ('code',)
    inlines = [ModelInlineAdmin]


class TypeAdmin(admin.ModelAdmin):
    model = Type
    fields = ('name', 'display_name')
    list_display = ('name', 'display_name')
    ordering = ('name',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ModelProduct, ModelProductAdmin)
admin.site.register(Clasification, ClasificationAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Type, TypeAdmin)