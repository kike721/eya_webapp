# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import Product, Family

def u8_decode(text_input):
    return text_input.decode('utf-8')

class Command(BaseCommand):
    help = "Fill catalog products"

    def handle(self, *args, **options):
        path_final = 'products/management/commands/final.csv'
        with open(path_final, 'rb') as data:
            rows = csv.reader(data, delimiter=',')
            i = 0
            for row in rows:
                if i > 0:
                    code_eyamex = row[2]
                    print code_eyamex
                    try:
                        product = Product.objects.get(code_eyamex=code_eyamex)
                        description = row[3]
                        quantity = row[6]
                        quantity_descr = row[7]
                        category = row[8]
                        family_desc = row[9]
                        try:
                            family = Family.objects.get(description=u8_decode(family_desc).lower())
                            product.family = family
                        except Exception as e:
                            pass
                        product.description = u8_decode(description)
                        product.quantity = u8_decode(quantity)
                        product.quantity_descr = u8_decode(quantity_descr)
                        product.category = u8_decode(category)
                        product.save()
                    except Exception as e:
                        print 'Error'
                        print e
                i += 1
