from django.db import models
from django.contrib.auth.models import AbstractUser

# local Django
from .managers import UserManager


class User(AbstractUser):
    user_manager = UserManager()
    username = None
    email = models.EmailField('Email', unique=True)
    first_name = models.CharField('First Name', max_length=30, blank=True)
    last_name = models.CharField('Surname', max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email