from comments.models import Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['articles_id', 'author_comm', 'text_comm', 'date_comm']

        widgets = {
            "articles_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
                'width': '500px'
            }),
            "author_comm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор комментария',
                'width': '500px'
            }),
            "full_comm": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст комментария',
                'width': '500px'
            }),
            "date_comm": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата комментария',
                'width': '500px'
            })
        }