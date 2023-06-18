from django.urls import path, include
from . import views


app_name = 'comments'


urlpatterns = [
    path('', views.CommentsView.as_view(), name='comm'),
]
