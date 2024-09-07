from django.contrib import admin  # Импортируем модуль admin для регистрации моделей в админ-панели

# Register your models here.
from.models import Post # Импортируем модель Post из текущего модуля (файла models.py)
admin.site.register(Post) # Регистрируем модель Post в админ-панели, чтобы её можно было управлять через интерфейс администратора


