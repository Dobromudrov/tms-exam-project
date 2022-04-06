from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
menu = ["Главная", "Прокат Авто", "Условия Аренды","О нас"]
# Меню через цикл (в проекте не используется)


def index(request):
    return render(request, 'main/index.html', {'menu': menu, 'title': 'Главная страница'})


def cars(request):
    posts = CarsTable.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Прокат Авто',
        'cat_selected': 0,
    }
    return render(request, 'main/cars.html', context=context)


def conditions(request):
    return render(request, 'main/conditions.html', {'menu': menu, 'title': 'Условия аренды'})


def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О нас'})


def show_category(request, cat_id):
    posts = CarsTable.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Прокат Авто',
        'cat_selected': cat_id,
    }

    return render(request, 'main/cars.html', context=context)


def register(request):
    return HttpResponse('Регистрация')


def login(request):
    return HttpResponse('Авторизация')


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = main/register.html
#     success_url = reverse_lazy('login')

