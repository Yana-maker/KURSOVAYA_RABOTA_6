from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    password = models.CharField(max_length=150, verbose_name='пароль')
    is_active = models.BooleanField(default=False)
    is_superuser = models.CharField(default=False, verbose_name='админ')
    is_staff = models.CharField(default=False, verbose_name='админ2')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='фото', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    code = models.CharField(max_length=150, verbose_name='код активации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


