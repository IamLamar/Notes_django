from django.urls import path # Импортируем функцию path для определения маршрутов
from . import views # Импортируем модуль views из текущей директории
urlpatterns = [
path('',views.post_list, name = 'post_list'),
]
# Определяем маршрут для корневого URL (''), который будет обрабатывать функция post_list из views.
# name='post_list' позволяет ссылаться на этот маршрут по имени в шаблонах и коде
