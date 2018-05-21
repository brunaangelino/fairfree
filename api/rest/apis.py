# -*- coding: UTF-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Fair
from api.filters import FairFilterSet
from api.rest.serializers import FairListSerializer, FairDetailSerializer


class FairList(ListCreateAPIView):
    queryset = Fair.objects.all()
    serializer_class = FairListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = FairFilterSet


class FairDetail(RetrieveUpdateDestroyAPIView):
    queryset = Fair.objects.all()
    serializer_class = FairDetailSerializer
    lookup_field = 'registro'