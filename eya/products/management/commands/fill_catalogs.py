# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import (Clasification, Color, Family, ModelProduct, Type)

class Command(BaseCommand):
    help = "Fill catalog products"

    def handle(self, *args, **options):
        path_catalog = 'products/management/commands/catalog.csv'
        types = list()
        clasifications = list()
        colors = dict()
        families = dict()
        models = list()
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            for row in rows:
                if i > 0:
                    # catalog types
                    if row[1] not in types and row[1] != '':
                        types.append(row[1])
                    # catalog clasification
                    if row[2] not in clasifications and row[2] != '':
                        clasifications.append(row[2])
                    # catalog families
                    if row[3] not in families.keys() and row[3] != '':
                        families[row[3]] = list()
                    # catalog models
                    if row[4] not in models and row[4] != '':
                        models.append(row[4])
                        if row[3] in families.keys():
                            mdls = families[row[3]]
                            mdls.append(row[4])
                            families[row[3]] = mdls
                    # colors
                    if row[6] not in colors.keys() and row[6] != '':
                        colors[row[6]] = row[7]
                i += 1
        print 'Begin fill types'
        for type_prod in types:
            obj, created = Type.objects.get_or_create(
                name=type_prod.lower(),
                display_name=type_prod.upper()
            )
        print 'End fill types'
        print 'Begin fill clasification'
        for clasification in clasifications:
            obj, created = Clasification.objects.get_or_create(
                name=clasification.lower(),
                display_name=clasification.upper()
            )
        print 'End fill clasification'
        print 'Begin fill colors'
        for color in colors:
            name = colors[color]
            obj, created = Color.objects.get_or_create(
                name=color.upper(),
                display_name=name.upper()
            )
        print 'End fill colors'
        print 'Begin fill families and models'
        for code in families:
            if not Family.objects.filter(code=code):
                family = Family.objects.create(code=code)
            else:
                family = Family.objects.filter(code=code)[0]
            for model in families[code]:
                obj, created = ModelProduct.objects.get_or_create(
                    code=model, family_product=family)
        print 'End fill families and models'