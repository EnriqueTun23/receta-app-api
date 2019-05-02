from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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