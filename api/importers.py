import abc
import os


class Importer(abc.ABC):

    def __init__(self, file_name):
        self.file_name = file_name

    @abc.abstractmethod
    def get_path(self):
        return ''

    def exists_file(self):
        path = self.get_path()
        return os.path.isfile(path)

    def import_from_filename(self, adaptor):
        path = self.get_path()
        adaptor.import_from_filename(path)


class CSVImporter(Importer):

    def get_path(self):
        return 'api/fixtures/FEIRAS_LIVRES/CSV/DEINFO_DADOS_AB_FEIRASLIVRES/%s' % self.file_name
