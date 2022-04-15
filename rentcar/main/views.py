from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class IndexPage(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Прокат Авто")
        return dict(list(context.items()) + list(c_def.items()))

# def index(request):
#     context = {
#         'menu': menu,
#         'title': 'Главная страница'
#     }
#     return render(request, 'main/index.html', context=context)
#     # return render(request, 'main/index.html', {'menu': menu, 'title': 'Главная страница'})


class CarsPage(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/cars.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        # cats = Category.objects.all()
        context = super().get_context_data(**kwargs)
        # context['cats'] = cats
        c_def = self.get_user_context(title="Прокат Авто")
        return dict(list(context.items()) + list(c_def.items()))

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


class ConditionsPage(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/conditions.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Условия аренды")
        return dict(list(context.items()) + list(c_def.items()))


# def conditions(request):
#     return render(request, 'main/conditions.html', {'menu': menu, 'title': 'Условия аренды'})

class AboutPage(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О нас")
        return dict(list(context.items()) + list(c_def.items()))

# def about(request):
#     return render(request, 'main/about.html', {'menu': menu, 'title': 'О нас'})


class AddCars(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addcars.html'
    success_url = reverse_lazy('cars')
    # login_url = '/admin/'
    login_url = reverse_lazy('index')
    # "success_url" - при добавлении записи ты будушь перенаправлен на указанный url
    # "reverse_lazy" - построение маршрута только в момент, когда понадобится
    # если "success_url" закомментирована, значит перенаправление будет на добавленную запись (ссылка на себя)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление машины")
        return dict(list(context.items()) + list(c_def.items()))


# def add_cars(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cars')
#     else:
#         form = AddPostForm()
#     return render(request, 'main/addcars.html', {'form': form, 'menu': menu, 'title': 'Добавить машину'})


class ShowPost(DataMixin, DetailView):
    model = CarsTable
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

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


class CarsCategory(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/cars.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return CarsTable.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

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


