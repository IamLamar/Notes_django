from django.db import models  # Импортируем модуль models, который предоставляет базовые классы для определения моделей в Django

# Create your models here.
class Post(models.Model):  # Определяем класс Post, который наследуется от models.Model и представляет модель данных
    title = models.CharField(max_length=100)  # Поле для заголовка поста, тип данных - строка, максимальная длина 100 символов
    content = models.TextField()  # Поле для содержания поста, тип данных - текстовое поле без ограничения длины
    create_at = models.DateTimeField(auto_now_add=True)  
    # Поле для хранения даты и времени создания поста, auto_now_add=True автоматически устанавливает текущее время при создании записи

    def __str__(self):  # Метод, который определяет строковое представление объекта
        return self.title  # Возвращаем заголовок поста, чтобы он отображался в виде строки (например, в админ-панели)
