# -*- coding: UTF-8 -*-
from django.db import models


class Fair(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    long = models.CharField(max_length=10)
    lat = models.CharField(max_length=10)
    setcens = models.CharField(max_length=15)
    areap = models.CharField(max_length=13)
    coddist = models.CharField(max_length=9)
    distrito = models.CharField(max_length=18)
    codsubpref = models.CharField(max_length=2)
    subpref = models.CharField(max_length=25)
    regiao5 = models.CharField(max_length=6)
    regiao8 = models.CharField(max_length=7)
    nome = models.CharField(max_length=30)
    registro = models.CharField(max_length=6)
    logadouro = models.CharField(max_length=34)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=20)
    referencia = models.CharField(max_length=24)

    def __str__(self):
        return self.nome