from django.db import models
from news.models import Articles


class Comments(models.Model):
    articles_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author_comm = models.CharField('Автор комметария', max_length=64)
    text_comm = models.TextField('Текст комментария')
    date_comm = models.DateTimeField('Дата')

    def __str__(self):
        return self.author_comm

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
