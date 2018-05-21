# -*- coding: UTF-8 -*-
import json

from django.http import QueryDict
from django.test import TestCase, Client
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from api.models import Fair
from api.rest.serializers import FairListSerializer, FairDetailSerializer


class FairApiTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_all_fairs(self):
        self._create_five_fairs()
        fairs = Fair.objects.all()
        fair_serializer = FairListSerializer(fairs, many=True)

        url = reverse('api-fair-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, fair_serializer.data)

    def test_get_valid_single_fair(self):
        registro = '1234-5'
        nome = 'Feira Livre'
        fair = mixer.blend(Fair, registro=registro, nome=nome)
        serializer = FairDetailSerializer(fair)

        url = reverse('api-fair-detail', kwargs={'registro': registro})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.data['nome'], serializer.data['nome'])

    def test_get_valid_single_fair_with_parameter_distrito(self):
        self._create_five_fairs()

        distrito = 'Distrito'
        mixer.cycle(2).blend(Fair, distrito=distrito)
        fairs = Fair.objects.filter(distrito=distrito)
        fair_serializer = FairListSerializer(fairs, many=True)

        params = QueryDict('', mutable=True)
        params.update({'distrito': distrito})
        url = '{base_url}?{querystring}'.format(
            base_url=reverse('api-fair-list'),
            querystring=params.urlencode()
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, fair_serializer.data)

    def test_get_valid_single_fair_with_parameter_nome(self):
        self._create_five_fairs()

        nome = 'Nome'
        mixer.cycle(2).blend(Fair, nome=nome)
        fairs = Fair.objects.filter(nome=nome)
        fair_serializer = FairListSerializer(fairs, many=True)

        params = QueryDict('', mutable=True)
        params.update({'nome': nome})
        url = '{base_url}?{querystring}'.format(
            base_url=reverse('api-fair-list'),
            querystring=params.urlencode()
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, fair_serializer.data)

    def test_get_valid_single_fair_with_parameter_regiao5(self):
        self._create_five_fairs()

        regiao5 = 'Regiao 5'
        mixer.cycle(2).blend(Fair, regiao5=regiao5)
        fairs = Fair.objects.filter(regiao5=regiao5)
        fair_serializer = FairListSerializer(fairs, many=True)

        params = QueryDict('', mutable=True)
        params.update({'regiao5': regiao5})
        url = '{base_url}?{querystring}'.format(
            base_url=reverse('api-fair-list'),
            querystring=params.urlencode()
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, fair_serializer.data)

    def test_get_valid_single_fair_with_parameter_bairro(self):
        self._create_five_fairs()

        bairro = 'Bairro'
        mixer.cycle(2).blend(Fair, bairro=bairro)
        fairs = Fair.objects.filter(bairro=bairro)
        fair_serializer = FairListSerializer(fairs, many=True)

        params = QueryDict('', mutable=True)
        params.update({'bairro': bairro})
        url = '{base_url}?{querystring}'.format(
            base_url=reverse('api-fair-list'),
            querystring=params.urlencode()
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, fair_serializer.data)

    def _create_five_fairs(self):
        mixer.cycle(5).blend(Fair)

    def test_get_invalid_single_fair(self):
        registro_invalid = '123456'

        url = reverse('api-fair-detail', kwargs={'registro': registro_invalid})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_valid_fair(self):
        data = json.dumps({
            "registro": "4041-0",
            "id": "1",
            "long": "-46550164",
            "lat": "-23558733",
            "setcens": "355030885000091",
            "areap": "3550308005040",
            "coddist": "87",
            "distrito": "VILA FORMOSA",
            "codsubpref": "26",
            "subpref": "ARICANDUVA-FORMOSA-CARRAO",
            "regiao5": "Leste",
            "regiao8": "Leste 1",
            "nome": "VILA FORMOSA",
            "logadouro": "RUA MARAGOJIPE",
            "numero": "S/N",
            "bairro": "VL FORMOSA",
            "referencia": "TV RUA PRETORIA"
        })

        url = reverse('api-fair-list')
        response = self.client.post(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_fair(self):
        data = json.dumps({
            "registro": "",
            "id": "",
            "long": "",
            "lat": "",
            "setcens": "",
            "areap": "",
            "coddist": "",
            "distrito": "",
            "codsubpref": "",
            "subpref": "",
            "regiao5": "",
            "regiao8": "",
            "nome": "",
            "logadouro": "",
            "numero": "",
            "bairro": "",
            "referencia": ""
        })

        url = reverse('api-fair-list')
        response = self.client.post(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_valid_fair(self):
        registro = "4041-0"
        fair = mixer.blend(Fair, registro=registro)
        fair_serializer = FairDetailSerializer(fair)
        data = json.dumps({
            "registro": registro,
            "id": "1",
            "long": "-46550164",
            "lat": "-23558733",
            "setcens": "355030885000091",
            "areap": "3550308005040",
            "coddist": "87",
            "distrito": "VILA FORMOSA",
            "codsubpref": "26",
            "subpref": "ARICANDUVA-FORMOSA-CARRAO",
            "regiao5": "Leste",
            "regiao8": "Leste 1",
            "nome": "VILA FORMOSA",
            "logadouro": "RUA MARAGOJIPE",
            "numero": "S/N",
            "bairro": "VL FORMOSA",
            "referencia": "TV RUA PRETORIA"
        })

        url = reverse('api-fair-detail', kwargs={'registro': registro})
        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['registro'], fair_serializer.data['registro'])
        self.assertNotEqual(response.data, fair_serializer.data)

    def test_put_invalid_fair(self):
        registro = "4041-0"
        fair = mixer.blend(Fair, registro=registro)
        fair_serializer = FairDetailSerializer(fair)

        registro_invalid = "1111"
        data = json.dumps({
            "registro": registro_invalid,
            "id": "1",
            "long": "-46550164",
            "lat": "-23558733",
            "setcens": "355030885000091",
            "areap": "3550308005040",
            "coddist": "87",
            "distrito": "VILA FORMOSA",
            "codsubpref": "26",
            "subpref": "ARICANDUVA-FORMOSA-CARRAO",
            "regiao5": "Leste",
            "regiao8": "Leste 1",
            "nome": "VILA FORMOSA",
            "logadouro": "RUA MARAGOJIPE",
            "numero": "S/N",
            "bairro": "VL FORMOSA",
            "referencia": "TV RUA PRETORIA"
        })

        url = reverse('api-fair-detail', kwargs={'registro': registro})
        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['registro'], fair_serializer.data['registro'])
        self.assertNotEqual(response.data, fair_serializer.data)

    def test_valid_delete(self):
        registro = '1234-5'
        mixer.blend(Fair, registro=registro)

        url = reverse('api-fair-detail', kwargs={'registro': registro})
        response = self.client.delete(url, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Fair.objects.filter(registro=registro).exists())

    def test_invalid_delete(self):
        registro = '123456'

        url = reverse('api-fair-detail', kwargs={'registro': registro})
        response = self.client.delete(url, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)