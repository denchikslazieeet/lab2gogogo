from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('rental.urls')),  # Подключение маршрутов приложения rental
]
