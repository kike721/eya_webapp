# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import Product

def u8_decode(text_input):
    return text_input.decode('utf-8')


class Command(BaseCommand):
    help = "Fill products"

    def handle(self, *args, **options):
        path_catalog = 'products/management/commands/spent.csv'
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            print 'Begin update products spent'
            for row in rows:
                code_eyamex = row[0]
                print 'Codigo es'
                print code_eyamex
                products = Product.objects.filter(code_eyamex=code_eyamex)
                if len(products) > 0:
                    product = products[0]
                    print product
                    product.spent = True
                    product.save()
                i += 1
                if i > 5:
                    break
            print 'End update products spent'
