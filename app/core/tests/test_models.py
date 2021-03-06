from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@gmail.com', password='rootpassword'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'rootpassword'
        user = get_user_model().objects.create_user(
            email = email,
            password= password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """Test el email del nuevo usaurio es normalizado"""
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
    
    
    def test_new_user_invalid_email(self):
        """test creando un suario sin email errores """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
    
    
    def test_create_new_superuser(self):
        """Creando un nuevo super usuario test"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    

    def test_tag_str(self):
        """TEst the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
    

    def test_ingredient_str(self):
        """ Test the ingredient string respresentation"""
        ingrediente = models.Ingrediente.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
    
    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Receta.objects.create(
            user=sample_user(),
            title='salsa de bistec y champiñones',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)