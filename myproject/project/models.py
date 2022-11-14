from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.
# сущности - пользователь, заявка, категория

class User(AbstractUser):
    fname = models.CharField(max_length=150, verbose_name='Имя', null=False, blank=False)
    lname = models.CharField(max_length=150, verbose_name='Фамилия', null=True, blank=True)
    sname = models.CharField(max_length=150, verbose_name='Отчество', null=False, blank=False)
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True, null=False, blank=False)
    email = models.CharField(max_length=250, verbose_name='Почта', unique=True, null=False, blank=False)
    password = models.CharField(max_length=250, verbose_name='Пароль', null=False, blank=False)
    personal_data = models.BooleanField(default=False, blank=False, null=False,
                                        verbose_name='Согласие на обработку персональных данных')

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
    name = models.CharField(max_length=250, verbose_name='Название', null=False, blank=False)
    description = models.CharField(max_length=250, verbose_name='Описание', null=False, blank=False)
    Category = models.ForeignKey('project.Category', verbose_name='Категория', blank=False, null=False,
                                 on_delete=models.CASCADE)
    photo = models.ImageField(max_length=250, upload_to=get_name_file,
                              blank=False, null=False,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']),
                                          file_size])
    date = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)
    status_choices = [
        ('new', 'Новая'),
        ('done', 'Выполнено'),
        ('received', 'Принято в работу')
    ]
    status = models.CharField(max_length=250, verbose_name='Статус', choices=status_choices, default='New')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название',
                            choices=(('3d', '3D Дизайн'), ('2d', '2D Дизайн'), ('sketch', 'Эскиз')), null=False,
                            blank=False)

    def __str__(self):
        return self.name
