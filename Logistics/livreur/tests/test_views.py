from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Livreur, Vehicule, Circuit
from ..serializers import LivreurSerializer, VehiculeSerializer


class GetAllLivreurTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            "admintest",
            "admintest@admintest.com",
            "admintest"
        )
        self.client.login(username='admintest', password='admintest')

    def test_details(self):
        response = self.client.get('http://127.0.0.1:8000/livreur/api/v1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
