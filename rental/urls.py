from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('bikes/', views.bike_list, name='bike_list'),  # Список велосипедов
    path('bikes/<int:bike_id>/', views.bike_detail, name='bike_detail'),  # Детали велосипеда
    path('about/', views.about, name='about'),  # О нас
    path('contact/', views.contact, name='contact'),  # Контакты
]
