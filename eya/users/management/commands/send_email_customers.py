# -*- coding: utf-8 -*-
import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from users.models import Customer
from store.email import send_password_customer


def u8_decode(text_input):
    return text_input.decode('utf-8')


class Command(BaseCommand):
    help = 'Sending email with passwords'

    def handle(self, *args, **options):
        path_catalog = 'users/management/commands/clientes_2019.csv'
        with open(path_catalog, 'rb') as catalog:
            rows = csv.reader(catalog, delimiter=',')
            i = 0
            print 'Begin send emails'
            for row in rows:
                if i > 0:
                    if row[2] != '':
                        email = row[2]
                        password = row[3]
                        print email
                        print password
                        send_password_customer(email, password)
                i += 1
            print 'End send emails'