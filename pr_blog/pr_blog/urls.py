from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls', namespace='news')),
    path('auth/', include('auth.urls', namespace='auth')),
    path('main/', include('main.urls', namespace='main')),
    path('comments/', include('comments.urls', namespace='comments'))
]