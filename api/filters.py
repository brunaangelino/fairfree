# -*- coding: UTF-8 -*-
from django_filters import FilterSet, CharFilter

from api.models import Fair


class FairFilterSet(FilterSet):
    distrito = CharFilter(label='Distrito', lookup_expr='icontains')
    regiao5 = CharFilter(label='Região', lookup_expr='icontains')
    bairro = CharFilter(label='Bairro', lookup_expr='icontains')
    nome = CharFilter(label='Nome', lookup_expr='icontains')

    class Meta:
        model = Fair
        fields = ('distrito', 'regiao5', 'bairro', 'nome',)