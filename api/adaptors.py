# -*- coding: UTF-8 -*-
from adaptor import model

from api import models as models_api


class FairAdaptorModel(model.CsvDbModel):
    class Meta:
        dbModel = models_api.Fair
        delimiter = ","
        has_header = True
        exclude_id = False
