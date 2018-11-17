# -*- coding: utf-8 -*-

import csv
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.models import Q

from users.models import Customer
from utils.models import StateMx

STATES_MX = {
    'AGS': 1, 'BC': 2, 'BCS': 3,
    'CAM': 4, 'COA': 5, 'COL': 6,
    'CHS': 7, 'CHI': 8, 'CDM': 9,
    'DF': 9, 'DUR': 10, 'GTO': 11,
    'GRO': 12, 'HID': 13, 'JAL': 14,
    'MEX': 15, 'MCH': 16, 'MOR': 17,
    'NAY': 18, 'NL': 19, 'OAX': 20,
    'PUE': 21, 'QUE': 22, 'QR': 23,
    'SLP': 24, 'SIN': 25, 'SON': 26,
    'TAB': 27, 'TAM': 28, 'TLA': 29,
    'VER': 30, 'YUC': 31, 'ZAC': 32,
}


def u8_decode(text_input):
    return text_input.decode('utf-8')


def str_to_decimal(string):
    numbers = string.split(',')
    integer = int(numbers[0])
    decimal = 0.0
    if len(numbers) > 1:
        decimal = int(numbers[1]) / 100.0
    return round(Decimal(integer + decimal), 2)

class Command(BaseCommand):
    help = 'Load customers from catallog ./clientes.csv'

    def handle(self, *args, **options):
        path_catalog = 'users/management/commands/clientes.csv'
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            print 'Begin fill customers'
            for row in rows:
                data = dict()
                if i > 0:
                    if row[7] in STATES_MX:
                        data['code'] = row[1]
                        data['name'] = u8_decode(row[2])
                        data['balance'] = str_to_decimal(row[3])
                        data['name_foreign'] = u8_decode(row[4])
                        data['street'] = u8_decode(row[5])
                        data['zip_code'] = row[6] if len(row[6]) <= 5 else ''
                        data['state'] = StateMx.objects.get(pk=STATES_MX[row[7]])
                        data['city'] = u8_decode(row[8])
                        data['phone'] = row[9] if len(row[9]) <= 15 else row[9][:10]
                        data['code_employee'] = int(row[10])
                        data['phone_2'] = row[11] if len(row[11]) <= 15 else row[11][:10]
                        data['fax'] = row[12] if '@' not in row[12] else ''
                        data['mobile'] = row[13]
                        data['contact'] = u8_decode(row[14])
                        data['code_conditions_payment'] = int(row[15])
                        data['limit_credit'] = str_to_decimal(row[16])
                        data['limit_debt'] = str_to_decimal(row[17])
                        user, created = User.objects.get_or_create(
                            username=data['code'],
                            is_active=False)
                        data['user'] = user
                        # print data
                        if created:
                            created, customer = Customer.objects.get_or_create(**data)
                i += 1
            print 'End fill customers'