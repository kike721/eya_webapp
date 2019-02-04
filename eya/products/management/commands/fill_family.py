# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand

from products.models import Family

def u8_decode(text_input):
    return text_input.decode('utf-8')

class Command(BaseCommand):
    help = "Fill catalog family"

    def handle(self, *args, **options):
        path_final = 'products/management/commands/final.csv'
        families = []
        print 'Get diferent families'
        with open(path_final, 'rb') as data:
            rows = csv.reader(data, delimiter=',')
            i = 0
            for row in rows:
                if i > 0:
                    family = u8_decode(row[9].lower())
                    # print family
                    if family not in families:
                        families.append(family)
                i += 1
        print 'Start fill families'
        for family in families:
            obj, created = Family.objects.get_or_create(description=family)
        print 'End fill families'