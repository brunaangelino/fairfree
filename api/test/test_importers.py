# -*- coding: UTF-8 -*-
from django.test import TestCase

from api.importers import Importer, CSVImporter


class CSVImporterTest(TestCase):

    def test_get_path(self):
        csv_importer = CSVImporter('nome_do_arquivo')
        self.assertEqual(csv_importer.get_path(), 'api/fixtures/FEIRAS_LIVRES/CSV/DEINFO_DADOS_AB_FEIRASLIVRES/nome_do_arquivo')

    def test_csv_importer_is_instance_of_importer(self):
        csv_importer = CSVImporter('nome_do_arquivo')
        self.assertIsInstance(csv_importer, Importer)

