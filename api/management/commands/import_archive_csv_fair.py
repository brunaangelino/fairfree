# -*- coding: UTF-8 -*-
import os.path
from django.core.management.base import BaseCommand

from api.adaptors import FairAdaptor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_names', nargs='+', type=str)

    def handle(self, *args, **options):

        file_names = options['file_names']

        for file_name in file_names:
            path = 'api/archives/FEIRAS_LIVRES/CSV/DEINFO_DADOS_AB_FEIRASLIVRES/%s' % (file_name)

            if os.path.isfile(path):
                print('Importando arquivo "%s" ... Aguarde!' % file_name)

                with open(path) as archive:
                    FairAdaptor.import_data(data=archive)

                print('Arquivo "%s" importado.' % path)

            else:
                print('Diretório "%s" não encontrado.' % (path))