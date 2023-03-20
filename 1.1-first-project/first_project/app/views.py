from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
from os import listdir, path


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    # context и параметры render менять не нужно
    # подробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    files = []
    dirs = []
    current_directory = listdir()
    for item in current_directory:
        if path.isfile(item):
            files.append(f'{item}')
        else:
            dirs.append(f'{item}')
    msg = f'Содержимое рабочей директории:<p>---Files:<p>' \
          f'{" <p>".join(files)}<p>---Directories:<p>{" <p>".join(dirs)}'
    return HttpResponse(msg)
