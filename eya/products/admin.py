# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from products.models import (Clasification, Color, Family, ModelProduct, Product, Type)

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	model = Product
	fields = (
		'code_eyamex', 'image', 'type', 'clasification', 'model',
		'code', 'color', 'description', 'is_new', 'best_seller', 'spent')
	list_display = ('code_eyamex', 'description')
	ordering = ('code_eyamex',)
	search_fields = ('code_eyamex', 'code', 'model__code', 'description')

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