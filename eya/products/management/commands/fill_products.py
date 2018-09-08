# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import (Clasification, Color, ModelProduct, Product, Type)

def u8_decode(text_input):
    return text_input.decode('utf-8')


class Command(BaseCommand):
    help = "Fill products"

    def handle(self, *args, **options):
        path_catalog = 'products/management/commands/catalog.csv'
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            print 'Begin fill products without image'
            for row in rows:
                if i > 0:
                    if row[1] == '':
                        break
                    code_eyamex = row[0]
                    type_prod = Type.objects.get(name=row[1].lower())
                    clasification = Clasification.objects.get(name=row[2].lower())
                    color = Color.objects.get(name=row[6].upper())
                    model = ModelProduct.objects.get(code=row[4])
                    code = row[5]
                    description = u8_decode(row[8])
                    product, created = Product.objects.get_or_create(
                        code_eyamex=code_eyamex,
                        type=type_prod,
                        clasification=clasification,
                        model=model,
                        code=code,
                        color=color,
                        description=description,
                        is_new=0,
                        best_seller=0,
                        spent=0)
                i += 1
            print 'End fill products without image'
