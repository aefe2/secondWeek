from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# сущности - пользователь, заявка, категория

class User(AbstractUser):
    fname = models.CharField(max_length=150, verbose_name='Имя', blank=False)
    lname = models.CharField(max_length=150, verbose_name='Фамилия', blank=False)
    sname = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=250, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=250, verbose_name='Пароль', blank=False)
    data_processing = models.BooleanField(verbose_name='Согласие на обработку персональных данных', blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.fname
