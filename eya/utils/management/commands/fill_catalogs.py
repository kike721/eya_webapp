import csv

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from utils.models import StateMx, MunicipalityMx, LocalityMx


def u8(text_input):
    return text_input.decode('latin-1').encode('utf-8')


class Command(BaseCommand):
    help = 'Fill catalogs state, municipalities and localities'

    def handle(self, *args, **options):
        path = settings.BASE_DIR + '/utils/catalogs/catalogs.csv'
        print path
        with open(path, 'rU') as csvFile:
            readCSV = csv.reader(csvFile, dialect=csv.excel)
            index = 0
            print 'Fill states, municipalities and localities of Mexico'
            for row in readCSV:
                if index > 0:
                    data_state = {'key_state': row[0], 'name': u8(row[1])}
                    data_municipality = {'key_municipality': row[3], 'name': u8(row[4])}
                    data_locality = {'key_locality': row[5], 'name': u8(row[6])}
                    state, created = StateMx.objects.get_or_create(**data_state)
                    data_municipality['state'] = state
                    municipality, created = MunicipalityMx.objects.get_or_create(**data_municipality)
                    data_locality['municipality'] = municipality
                    locality, created = LocalityMx.objects.get_or_create(**data_locality)
                print '...',
                index += 1
        self.stdout.write(self.style.SUCCESS('Todo salio bien'))
