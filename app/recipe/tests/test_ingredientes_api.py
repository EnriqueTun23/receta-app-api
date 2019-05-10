from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingrediente

from recipe.serializers import IngredienteSerializer

INGREDIENTES_URL = reverse('recipe:ingrediente-list')

class PublicIngredientsApiTests(TestCase):
    """TEst the publicly available ingrediebts API"""

    def  setUp(self):
        self.client = APIClient()
    
    def test_login_required(self):
        """Test that login is required to access the endpoint"""
        res = self.client.get(INGREDIENTES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateIngredientsApiTests(TestCase):
    """Test the private ingredientes API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)
    
    def test_retrieve_ingredient_list(self):
        """Test retrieving a list of ingredientes"""
        Ingrediente.objects.create(user=self.user, name='kale')
        Ingrediente.objects.create(user=self.user, name='Salt')

        res = self.client.get(INGREDIENTES_URL)

        ingredientes = Ingrediente.objects.all().order_by('-name')
        serializer = IngredienteSerializer(ingredientes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    
    def test_ingredientes_limited_to_user(self):
        """Test that ingredientes for the authentificated user are retured """

        user2 = get_user_model().objects.create_user(
            'other@gmail.com',
            'testpass'
        )
        Ingrediente.objects.create(user=user2, name='inegar')
        ingredient = Ingrediente.objects.create(user=self.user, name='Tumeric')

        res = self.client.get(INGREDIENTES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)