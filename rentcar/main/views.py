from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


menu = [{'title': 'Главная страница', 'url_name': 'index'},
    {'title': 'Прокат Авто', 'url_name': 'cars'},
    {'title': 'Условия Аренды', 'url_name': 'conditions'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Добавить машину', 'url_name': 'add_cars'},
    {'title': 'Регистрация', 'url_name': 'register'},
    {'title': 'Войти', 'url_name': 'login'},

]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', context=context)
    # return render(request, 'main/index.html', {'menu': menu, 'title': 'Главная страница'})


class CarsPage(ListView):
    model = CarsTable
    template_name = 'main/cars.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        cats = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Прокат Авто'
        context['cat_selected'] = 0
        context['cats'] = cats
        return context

    def get_queryset(self):
        return CarsTable.objects.filter(is_published=True)

# def cars(request):
#     posts = CarsTable.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Прокат Авто',
#         'cat_selected': 0,
#     }
#     return render(request, 'main/cars.html', context=context)


def conditions(request):
    return render(request, 'main/conditions.html', {'menu': menu, 'title': 'Условия аренды'})


def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О нас'})


class AddCars(CreateView):
    form_class = AddPostForm
    template_name = 'main/addcars.html'
    success_url = reverse_lazy('cars')
    # "success_url" - при добавлении записи ты будушь перенаправлен на указанный url
    # "reverse_lazy" - построение маршрута только в момент, когда понадобится
    # если "success_url" закомментирована, значит перенаправление будет на добавленную запись (ссылка на себя)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление машины'
        context['menu'] = menu
        return context


# def add_cars(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cars')
#     else:
#         form = AddPostForm()
#     return render(request, 'main/addcars.html', {'form': form, 'menu': menu, 'title': 'Добавить машину'})


class ShowPost(DetailView):
    model = CarsTable
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

# def show_post(request, post_slug):
#     post = get_object_or_404(CarsTable, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'main/post.html', context=context)


class CarsCategory(ListView):
    model = CarsTable
    template_name = 'main/cars.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return CarsTable.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_id):
#     posts = CarsTable.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Прокат Авто',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'main/cars.html', context=context)


def register(request):
    return HttpResponse('Регистрация')


def login(request):
    return HttpResponse('Авторизация')


