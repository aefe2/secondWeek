from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import HiddenInput, inlineformset_factory

from project.models import User, Aplication


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', validators=[
        RegexValidator('^[a-zA-Z-]+$', message='Разрешены только латиница и дефис')], error_messages={
        'required': 'Обязательное поле',
        'unique': 'Данный логин занят'
    })
    email = forms.EmailField(label='Почта', error_messages={
        'invalid': 'Не правильный формат адреса почты',
        'unique': 'Данная почта занята'
    })
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, error_messages={
        'required': 'Обязательное поле'
    })
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput, error_messages={
        'required': 'Обязательное поле'
    })
    fname = forms.CharField(label='Имя', validators=[
        RegexValidator('^[а-яА-Я- ]+$', message='В поле имя может быть только кириллица, дефис или пробел')],
                            error_messages={'required': 'Обязательное поле'})

    lname = forms.CharField(label='Фамилия', validators=[
        RegexValidator('^[а-яА-Я- ]+$', message='В поле фамилия может быть только кириллица, дефис или пробел')],
                            error_messages={'required': 'Обязательное поле'})

    sname = forms.CharField(label='Отчество', validators=[
        RegexValidator('^[а-яА-Я- ]+$', message='В поле отчество может быть только кириллица, дефис или пробел')],
                            error_messages={'required': 'Обязательное поле'})

    personal_data = forms.BooleanField(required=True, label='Согласие на обработку персональных данных',
                                       error_messages={'required': 'Обязательное поле'})

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Введенные пароли не совпадают', code='password_missmatch')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'fname', 'lname', 'sname', 'personal_data')


class CreateAplForm(forms.ModelForm):
    photo = forms.ImageField(label='Фото', )

    class Meta:
        model = Aplication
        fields = ('name', 'description', 'Category', 'photo')
        enctype = "multipart/form-data"


class AplicationForm(forms.ModelForm):
    def clean(self):
        status = self.cleaned_data.get('status')
        comment = self.cleaned_data.get('comment')
        second_photo = self.cleaned_data.get('second_photo')
        if self.instance.status != 'new':
            raise forms.ValidationError({'status': 'Статус можно сменить только у новой заявки'})
        if status == 'new' and comment:
            raise forms.ValidationError({'comment': 'К новой заявке нельзя добавить комментарий'})
        if status == 'received' and not comment:
            raise forms.ValidationError({'comment': 'Нужно указать комментарий для заявки принятой в работу'})
        if status == 'done' and not second_photo:
            raise forms.ValidationError({'second_photo': 'Нужно добавить фотографию для выполненой заявки'})
