from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request): # Определяем функцию post_list, которая принимает HTTP-запрос
    posts = Post.objects.all()# Получаем все записи из класса Post
    return render(request,'post_list.html',{'posts':posts})
    # Возвращаем HTML-страницу, отрендеренную с использованием шаблона 'post_list.html',
    # и передаем в шаблон список всех постов в переменной 'posts'

