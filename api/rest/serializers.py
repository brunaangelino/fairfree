# -*- coding: UTF-8 -*-
from rest_framework.serializers import ModelSerializer, CharField

from api.models import Fair


class FairListSerializer(ModelSerializer):
    class Meta:
        model = Fair
        fields = '__all__'


class FairListSerializer(FairListSerializer):
    pass


class FairDetailSerializer(FairListSerializer):
    registro = CharField(max_length=6, read_only=True)
