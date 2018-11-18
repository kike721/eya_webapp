# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.models import Q

from products.models import Product
from store.models import DetailOrder, Order
from users.models import Customer

def u8_decode(text_input):
    return text_input.decode('utf-8')


def str_to_decimal(string):
    numbers = string.split(',')
    integer = int(numbers[0])
    decimal = 0.0
    if len(numbers) > 1:
        decimal = int(numbers[1]) / 100.0
    return round(Decimal(integer + decimal), 2)

def str_to_int(string):
    numbers = string.split(',')
    return int(numbers[0])

class Command(BaseCommand):
    help = 'Load customers from catallog ./clientes.csv'

    def handle(self, *args, **options):
        path_catalog = 'users/management/commands/historico.csv'
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            o = 0
            print 'Begin fill history customers'
            status = 'F'
            for row in rows:
                if i > 0:
                    date = row[2]
                    date_order = datetime.strptime(date, '%d/%m/%Y')
                    # Get customer verify if exists
                    code_customer = row[3]
                    customer = Customer.objects.filter(code=code_customer)
                    customer = customer[0] if len(customer) > 0 else None
                    # Get product verify if exists
                    code_product = row[4]
                    product = Product.objects.filter(code_eyamex=code_product)
                    product = product[0] if len(product) > 0 else None
                    quantity = str_to_int(row[5])
                    price = str_to_decimal(row[6])
                    discount = str_to_int(row[7])
                    data_order = {'created': date_order, 'modified': date_order,
                                  'customer': customer, 'status': status}
                    data_detailOrder = {'product': product,
                                        'quantity': quantity, 'price': price,
                                        'created': date_order, 'modified': date_order,
                                        'discount': discount}
                    if customer and product and quantity > 0:
                        order, is_created = Order.objects.get_or_create(**data_order)
                        data_detailOrder['order'] = order
                        detailOrder = DetailOrder.objects.get_or_create(**data_detailOrder)
                        o += 1
                i += 1
                # if o > 0:
                #     break
            print 'End fill history customers'