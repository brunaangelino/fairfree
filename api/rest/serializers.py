# -*- coding: UTF-8 -*-
from rest_framework.serializers import ModelSerializer, CharField

from api.models import Fair


class FairSerializer(ModelSerializer):
    class Meta:
        model = Fair
        fields = '__all__'


class FairListSerializer(FairSerializer):
    pass


class FairDetailSerializer(FairSerializer):
    registro = CharField(max_length=6, read_only=True)
