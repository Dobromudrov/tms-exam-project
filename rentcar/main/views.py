from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import *
from .models import *
from .utils import *


class IndexPage(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


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


class ConditionsPage(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/conditions.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Условия аренды")
        return dict(list(context.items()) + list(c_def.items()))


class ContactsPage(DataMixin, ListView):
    model = CarsTable
    template_name = 'main/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Контакты")
        return dict(list(context.items()) + list(c_def.items()))


class AddCars(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    permission_required = ''
    form_class = AddPostForm
    template_name = 'main/addcars.html'
    success_url = reverse_lazy('cars')
    # login_url = '/admin/'
    login_url = reverse_lazy('logins')
    # login_url перенаправляет на указанную страницу, если ты не авторизован
    # "success_url" - при добавлении записи ты будушь перенаправлен на указанный url
    # "reverse_lazy" - построение маршрута только в момент, когда понадобится
    # если "success_url" закомментирована, значит перенаправление будет на добавленную запись (ссылка на себя)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление машины")
        return dict(list(context.items()) + list(c_def.items()))


class UpdatePost(PermissionRequiredMixin, DataMixin, UpdateView):
    permission_required = ''
    form_class = AddPostForm
    model = CarsTable
    template_name = 'main/update_cars.html'
    slug_url_kwarg = 'post_slug'
    # success_url = reverse_lazy('cars')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Изменение поста')
        return dict(list(context.items()) + list(c_def.items()))


class DeletePost(PermissionRequiredMixin, DataMixin, DeleteView):
    permission_required = ''
    model = CarsTable
    template_name = 'main/delete_cars.html'
    # form_class = AddPostForm
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('cars')
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление поста")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(LoginRequiredMixin, DataMixin, DetailView):
    model = CarsTable
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    login_url = reverse_lazy('login')
    # login_url перенаправляет на указанную страницу, если ты не авторизован

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class PostOrder(LoginRequiredMixin, DataMixin, CreateView):
    form_class = OrderPostForm
    template_name = 'main/ordering.html'
    success_url = reverse_lazy('cars')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Заказ машины")
        return dict(list(context.items()) + list(c_def.items()))


class Application(PermissionRequiredMixin, DataMixin, ListView):
    paginate_by = 3
    permission_required = ''
    model = OrderTable
    template_name = 'main/processing_of_applications.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обработка заявок")
        return dict(list(context.items()) + list(c_def.items()))


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


class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm
    # Стандартная форма регистрации от django
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('cars')


def logout_user(request):
    logout(request)
    return redirect('login')








