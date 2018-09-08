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
        images = []
        cont = 0
        for d in dirs:
            path_products = '{}/{}'.format(path_dir_images,d)
            products = os.listdir(path_products)
            for product in products:
                path_image = '{}/{}'.format(path_products, product)
                if isdir(path_image):
                    products_2 = os.listdir(path_image)
                    for img in products_2:
                        path_image_2 = '{}/{}'.format(path_image, img)
                        code_eyamex = img.split('.')[0]
                        cont += 1
                        images.append(code_eyamex)
                else:
                    path_image = '{}/{}'.format(path_products, product)
                    code_eyamex = product.split('.')[0]
                    cont += 1
                    images.append(code_eyamex)
        with open('images_2.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['Total', len(images)])
            print len(images)
            print cont
            for image in images:
                writer.writerow([image])
        print 'Imagenes actualizadas reporte'