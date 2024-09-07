from django.apps import AppConfig  # Импортируем класс AppConfig, который используется для конфигурации приложения в Django

class PostConfig(AppConfig):  # Определяем класс конфигурации приложения, наследуемый от AppConfig
    default_auto_field = 'django.db.models.BigAutoField'  
    # Устанавливаем тип поля по умолчанию для автоматически создаваемого первичного ключа (ID) в модели, используем BigAutoField для больших числовых значений
    name = 'post'  # Указываем имя приложения, которое должно совпадать с именем директории приложения
