from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', CarsPage.as_view(), name='cars'),
    path('conditions/', views.conditions, name='conditions'),
    path('about/', views.about, name='about'),
    path('add_cars/', AddCars.as_view(), name='add_cars'),
    path('cars/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarsCategory.as_view(), name='category'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
