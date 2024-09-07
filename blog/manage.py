#!/usr/bin/env python3
# Специальная строка для указания интерпретатора Python, который будет использоваться для выполнения скрипта

"""Django's command-line utility for administrative tasks."""
# Документальная строка, описывающая назначение этого скрипта: утилита командной строки Django для выполнения административных задач

import os  # Импортируем модуль os для работы с операционной системой
import sys  # Импортируем модуль sys для взаимодействия с интерпретатором Python

def main():
    """Run administrative tasks."""
    # Функция main, которая выполняет административные задачи
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
    # Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE, которая указывает на файл настроек Django проекта (blog.settings)

    try:
        from django.core.management import execute_from_command_line
        # Импортируем функцию execute_from_command_line, которая обрабатывает командную строку и запускает соответствующие команды Django
    except ImportError as exc:
        # Если возникает ошибка импорта, обрабатываем её
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
            # Выводим сообщение об ошибке, если Django не установлен или не доступен в PYTHONPATH, или если забыли активировать виртуальное окружение
        ) from exc
    
    execute_from_command_line(sys.argv)
    # Передаем аргументы командной строки в функцию execute_from_command_line, чтобы выполнить соответствующую команду Django

if __name__ == '__main__':
    main()
    # Если скрипт выполняется напрямую (а не импортируется как модуль), вызываем функцию main()

