from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.crypto import get_random_string


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


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл слишком большой, он не должен весить больше 2Mb')


class Aplication(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название', blank=False)
    description = models.CharField(max_length=250, verbose_name='Описание', blank=False)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    photo = models.ImageField(max_length=250, upload_to=get_name_file,
                              blank=False, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']),
                                          file_size])

    def __str__(self):
        return self.name


class Category:
    name = models.CharField(max_length=250, verbose_name='Название', blank=False)

    def __str__(self):
        return self.name
