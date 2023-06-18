from django.urls import path, include
from . import views


app_name = 'news'


urlpatterns = [
    path('', views.NewsHomeView.as_view(), name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
]
