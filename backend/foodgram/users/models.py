from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=254,
        verbose_name='email',
        help_text='Введите электронную почту')
    username = models.CharField(
        db_index=True,
        max_length=150,
        unique=True,
        verbose_name='username',
        help_text='Введите уникальное имя пользователя')
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        help_text='Введите имя пользователя')
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        help_text='Введите фамилию пользователя')
    is_subscribed = models.BooleanField(
        default=False,
        verbose_name='Подписка на данного пользователя',
        help_text='Подписка на данного пользователя')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    def __str__(self):
        return self.username
