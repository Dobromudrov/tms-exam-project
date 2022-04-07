from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'index'},
    {'title': 'Прокат Авто', 'url_name': 'cars'},
    {'title': 'Условия Аренды', 'url_name': 'conditions'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Добавить машину', 'url_name': 'add_cars'},
    {'title': 'Регистрация', 'url_name': 'register'},
    {'title': 'Войти', 'url_name': 'login'},

]

# menu = ["Главная", "Прокат Авто", "Условия Аренды", "О нас", "Добавить Машину", "Войти"]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', context=context)
    # return render(request, 'main/index.html', {'menu': menu, 'title': 'Главная страница'})


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


def add_cars(request):
    return HttpResponse("Добавить машину")


def show_post(request, post_id):
    # return HttpResponse(f"Отображение статьи с id = {post_id}")
    post = get_object_or_404(CarsTable, pk=post_id)

    context= {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'main/post.html', context=context)


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

