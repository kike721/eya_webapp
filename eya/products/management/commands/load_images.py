# -*- coding: utf-8 -*-
import csv
import os
from os.path import isdir

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
            if isdir(path_products):
                products = os.listdir(path_products)
                for product in products:
                    path_image = '{}/{}'.format(path_products, product)
                    if isdir(path_image):
                        products_2 = os.listdir(path_image)
                        for img in products_2:
                            path_image_2 = '{}/{}'.format(path_image, img)
                            code_eyamex = img.split('.')[0]
                            try:
                                obj = Product.objects.get(code_eyamex=code_eyamex)
                            except Exception as e:
                                obj = None
                            if obj:
                                obj.image = File(open(path_products, 'r'))
                                obj.save()
                                # if not obj.image:
                                #     obj.image = File(open(path_image_2, 'r'))
                                #     obj.save()
                    else:
                        path_image = '{}/{}'.format(path_products, product)
                        code_eyamex = product.split('.')[0]
                        try:
                            obj = Product.objects.get(code_eyamex=code_eyamex)
                        except Exception as e:
                            obj = None
                        if obj:
                            obj.image = File(open(path_products, 'r'))
                            obj.save()
                            # if not obj.image:
                            #     obj.image = File(open(path_image, 'r'))
                            #     obj.save()
            else:
                code_eyamex = d.split('.')[0]
                try:
                    obj = Product.objects.get(code_eyamex=code_eyamex)
                except Exception as e:
                    obj = None
                if obj:
                    obj.image = File(open(path_products, 'r'))
                    obj.save()
                    # if not obj.image:
                    #     obj.image = File(open(path_products, 'r'))
                    #     obj.save()
        print 'Imagenes actualizadas'