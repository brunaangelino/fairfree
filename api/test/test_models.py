# -*- coding: UTF-8 -*-
from mixer.backend.django import mixer
from django.test import TestCase

from api.models import Fair


class TestFair(TestCase):

    def setUp(self):
        self.fair = mixer.blend(Fair, nome='Feira Livre')

    def test_fair_creation(self):
        self.assertIsInstance(self.fair, Fair)

    def test_fair_str(self):
        self.assertEqual(self.fair.__str__(), self.fair.nome)

