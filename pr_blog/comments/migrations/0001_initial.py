# Generated by Django 4.1.3 on 2023-06-17 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0003_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_comm', models.CharField(max_length=64, verbose_name='Автор комметария')),
                ('text_comm', models.TextField(verbose_name='Текст комментария')),
                ('date_comm', models.DateTimeField(verbose_name='Дата')),
                ('articles_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.articles')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
