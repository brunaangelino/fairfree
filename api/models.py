# -*- coding: UTF-8 -*-
from django.db import models


class Fair(models.Model):
    id = models.CharField(max_length=8, verbose_name='Identificação')
    long = models.CharField(max_length=10, verbose_name='Longitude')
    lat = models.CharField(max_length=10, verbose_name='Latitude')
    setcens = models.CharField(max_length=15, verbose_name='Setor censitário')
    areap = models.CharField(max_length=13, verbose_name='Área de ponderação')
    coddist = models.CharField(max_length=9, verbose_name='Código do distrito')
    distrito = models.CharField(max_length=18, verbose_name='Distrito municipal')
    codsubpref = models.CharField(max_length=2, verbose_name='Código da subprefeitura')
    subpref = models.CharField(max_length=25, verbose_name='Subprefeitura')
    regiao5 = models.CharField(max_length=6, verbose_name='Região conforme divisão do município em 5 áreas')
    regiao8 = models.CharField(max_length=7, verbose_name='Região conforme divisão do município em 8 áreas')
    nome = models.CharField(max_length=30, verbose_name='Nome da feira livre')
    registro = models.CharField(max_length=6, primary_key=True, verbose_name='Registro da feira livre')
    logadouro = models.CharField(max_length=34, verbose_name='Logradouro')
    numero = models.CharField(max_length=5, verbose_name='Número')
    bairro = models.CharField(max_length=20, verbose_name='Bairro')
    referencia = models.CharField(max_length=24, verbose_name='Ponto de referência')

    def __str__(self):
        return self.nome