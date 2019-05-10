from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings
# Create your models here.

class AdministradorUsuarios(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Crear y guardar un nuevo usuario"""
        if not email:
            raise ValueError('Usuario necesita un email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Crear y guardar un nuevo super usuarios"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    """Modelo de usuario personalizado que admite el uso del 
    correo electrónico en  lugar del nombre de usuario."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = AdministradorUsuarios()
    USERNAME_FIELD = 'email'


class Tag(models.Model):
    """Tag to be used for recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )

    def __str__(self):
        return self.name


class Ingrediente(models.Model):
    """ingredientes se usara para el recipiente"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Receta(models.Model):
    """Receta objetos"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title  = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    ingredintes = models.ManyToManyField('Ingrediente')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title