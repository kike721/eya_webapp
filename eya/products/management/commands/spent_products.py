# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import Product

class Command(BaseCommand):
    help = "Update spent products"

    def handle(self, *args, **options):
        path_final = 'products/management/commands/Faltantes.csv'
        with open(path_final, 'rb') as data:
            rows = csv.reader(data, delimiter=',')
            i = 0
            for row in rows:
                if i > 0:
                    code_eyamex = row[0]
                    print code_eyamex
                    try:
                        product = Product.objects.get(code_eyamex=code_eyamex)
                        product.spent = True
                        product.save()
                        print 'Se marco como agotado ' + code_eyamex
                    except Exception as e:
                        print 'Error'
                        print e
                i += 1
