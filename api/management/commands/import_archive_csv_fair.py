# -*- coding: UTF-8 -*-
import os.path
from django.core.management.base import BaseCommand
from adaptor.model import CsvDataException

from api.adaptors import FairAdaptorModel
from api.importers import CSVImporter


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_names', nargs='+', type=str)

    def handle(self, *args, **options):

        file_names = options['file_names']

        for file_name in file_names:
            csv_importer = CSVImporter(file_name)

            if csv_importer.exists_file():
                print('Importando arquivo "%s" ... Aguarde!' % file_name)
                try:
                    csv_importer.import_from_filename(FairAdaptorModel)
                except CsvDataException:
                    print('Arquivo "%s" importado.' % file_name)

            else:
                print('Arquivo %s não encontrado.' % (file_name))