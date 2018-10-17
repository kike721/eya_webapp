# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import (Clasification, Color, ModelProduct, Product, Type)

def u8_decode(text_input):
    return text_input.decode('utf-8')


class Command(BaseCommand):
    help = "Fill description families"

    def handle(self, *args, **options):
        path_catalog = 'products/management/commands/families.csv'
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            print 'Begin fill description families'
            for row in rows:
                if i > 0:
                    code_eyamex = row[2]
                    family_description = u8_decode(row[4])
                    query = Product.objects.filter(code_eyamex=code_eyamex)
                    if len(query) > 0:
                        family = query[0].model.family_product
                        family.description = family_description
                        family.save()
                        query[0].save()
                i += 1
            print 'End fill description families'
