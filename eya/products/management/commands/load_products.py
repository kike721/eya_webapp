# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import (Clasification, Color, Product, Family)

def u8_decode(text_input):
    return text_input.decode('utf-8')


class Command(BaseCommand):
    help = "Fill products"

    def handle(self, *args, **options):
        path_catalog = 'products/management/commands/productos_completos.csv'
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            print 'Begin fill products without image'
            for row in rows:
                if i > 0:
                    code_eyamex = row[2]
                    # type_prod = Type.objects.get(name=row[1].lower())
                    clasification = Clasification.objects.get(name=row[0].lower())
                    family = Family.objects.get(description=u8_decode(row[9]))
                    color = Color.objects.get(name=row[4].upper())
                    code = '-'.join(code_eyamex.split('-')[:-1])
                    description = u8_decode(row[3])
                    product, created = Product.objects.get_or_create(
                        code_eyamex=code_eyamex,
                        clasification=clasification,
                        family=family,
                        code=code,
                        color=color,
                        description=description,
                        is_new=0,
                        best_seller=0,
                        spent=0)
                    if (created):
                        print 'Se creo el siguiente producto'
                        print product
                i += 1
            print 'End fill products without image'
