from django.urls import path, include
from . import views


app_name = 'main'


urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('about_us', views.about_us_view, name='about_us'),
    path('contact', views.contact_view, name='contact'),
]
