# -*- coding: utf-8 -*-
import csv
import os

from django.core.files import File
from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):
    help = "Fill products"

    def handle(self, *args, **options):
        path_dir_images = 'products/management/commands/imagenes'
        dirs = os.listdir(path_dir_images)
        print 'Actualizando imagenes'
        for d in dirs:
        	path_products = '{}/{}'.format(path_dir_images,d)
        	products = os.listdir(path_products)
        	for product in products:
        		path_image = '{}/{}'.format(path_products, product)
        		code_eyamex = product.split('.')[0]
        		# print code_eyamex
        		try:
        			obj = Product.objects.get(code_eyamex=code_eyamex)
        		except Exception as e:
        			obj = None
        		if obj:
        			print obj.code_eyamex
        			obj.image = File(open(path_image, 'r'))
        			obj.save()
        print 'Imagenes actualizadas'