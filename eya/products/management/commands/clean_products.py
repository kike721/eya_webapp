# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import Product, Family, Clasification, Color

def u8_decode(text_input):
    return text_input.decode('utf-8')

class Command(BaseCommand):
    help = "Remove products if not exists in catalog"

    def handle(self, *args, **options):
        path_final = 'products/management/commands/final.csv'
        products = Product.objects.all()
        products_db = []
        for product in products:
            # if product.code_eyamex not in products_catalog:
            #     print 'No existe'
            #     print product
            #     print product.delete()
            products_db.append(product.code_eyamex)
        with open(path_final, 'rb') as data:
            rows = csv.reader(data, delimiter=',')
            i = 0
            for row in rows:
                if i > 0:
                    if row[2] not in products_db:
                        print 'Falta este producto'
                        print row[2]
                        code_eyamex = row[2]
                        clasification, created = Clasification.objects.get_or_create(
                            name=row[0].lower(), display_name=row[0])
                        color, created = Color.objects.get_or_create(name=row[4].upper(), display_name=u8_decode(row[5].upper()))
                        code = row[2][:15]
                        description = u8_decode(row[3])
                        quantity = row[6].replace(',', '.')
                        quantity_descr = u8_decode(row[7])
                        category = u8_decode(row[8].lower())
                        family = Family.objects.get(description=u8_decode(row[9].lower()))
                        product, created = Product.objects.get_or_create(
                            code_eyamex=code_eyamex,
                            clasification=clasification,
                            code=code,
                            color=color,
                            family=family,
                            description=description,
                            is_new=0,
                            home_is_new=0,
                            best_seller=0,
                            home_best_seller=0,
                            spent=0,
                            quantity=quantity,
                            quantity_descr=quantity_descr,
                            category=category)
                i += 1