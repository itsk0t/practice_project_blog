from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['author', 'title', 'anons', 'full_text', 'date']

        widgets = {
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор',
                'width': '500px'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
                'width': '500px'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
                'width': '500px'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
                'width': '500px'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
                'width': '500px'
            }),
        }


