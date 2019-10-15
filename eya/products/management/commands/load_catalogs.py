# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import (Clasification, Color, Family)

def u8_decode(text_input):
    return text_input.decode('utf-8')

class Command(BaseCommand):
    help = "Fill catalog products"

    def handle(self, *args, **options):
        path_catalog = 'products/management/commands/productos_completos.csv'
        clasifications = list()
        colors = dict()
        families = list()
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            for row in rows:
                if i > 0:
                    # catalog clasifications
                    if u8_decode(row[0]) not in clasifications and row[0] != '':
                        clasifications.append(u8_decode(row[0]))
                    # catalog families
                    if u8_decode(row[9]) not in families and row[9] != '':
                        families.append(u8_decode(row[9]))
                    # colors
                    if u8_decode(row[4]) not in colors.keys() and row[4] != '':
                        colors[u8_decode(row[4])] = u8_decode(row[5])
                i += 1
        # print clasifications
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
        print 'Begin fill families'
        for family in families:
            obj, created = Family.objects.get_or_create(
                description=family.lower(),
            )
        print 'End fill families'
