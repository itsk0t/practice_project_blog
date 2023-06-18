from django import forms as dj_forms
from django.contrib.auth import forms
from django.forms import TextInput, PasswordInput

from auth.models import CustomUser


class CustomUserRegister(forms.UserCreationForm):
    username = dj_forms.CharField(max_length=32,
                                  min_length=6,
                                  label='Логин')
    email = dj_forms.EmailField(max_length=128,
                                min_length=8,
                                label='Электронная почта')
    first_name = dj_forms.CharField(max_length=32,
                                    min_length=4,
                                    label='Имя')
    last_name = dj_forms.CharField(max_length=32,
                                   min_length=4,
                                   label='Фамилия')
    password1 = dj_forms.CharField(widget=dj_forms.PasswordInput,
                                   label='Пароль')
    password2 = dj_forms.CharField(widget=dj_forms.PasswordInput,
                                   label='Повторите пароль')

    class Meta:
        model = CustomUser
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'
            item.help_text = ''

    widgets = {
        "username": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя',
            'width': '500px'
        }),
        "first_name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя',
            'width': '500px'
        }),
        "last_name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия',
            'width': '500px'
        }),
        "email": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Эл. почта',
            'width': '500px'
        }),
        "password1": PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'width': '500px'
        }),
        "password2": PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повтор пароля',
            'width': '500px'
        }),
    }