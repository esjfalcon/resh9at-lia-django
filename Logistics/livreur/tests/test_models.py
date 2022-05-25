import unittest
from django.test import TestCase
from ..models import Livreur, Vehicule, Circuit


class LivreurTest(TestCase):
    def setUp(self):
        Livreur.objects.create(
            name="hamza", age=27)

    def test_check_if_livreur_with_name_hamza_created(self):
        livreur_hamza = Livreur.objects.get(name='hamza')
        self.assertTrue(livreur_hamza)

    @unittest.expectedFailure
    def test_check_if_livreur_with_name_oussama_not_created(self):
        livreur_oussama = Livreur.objects.get(name='oussama')
        self.assertTrue(livreur_oussama)
