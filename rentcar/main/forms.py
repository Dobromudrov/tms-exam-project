from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255,label="Модель машины")
#     slug = forms.SlugField(max_length=255, label="URL")
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Описание")
#     is_published = forms.BooleanField(label="Статус публикации", required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")


class AddPostForm(forms.ModelForm):
    class Meta:
        model = CarsTable
        fields = ['title', 'slug', 'content', 'price', 'photo', 'is_published', 'cat']


class OrderPostForm(forms.ModelForm):
    class Meta:
        model = OrderTable
        fields = ['name', 'phone_number', 'comment']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackTable
        fields = ['email', 'comment']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # number_client = forms.TextField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))