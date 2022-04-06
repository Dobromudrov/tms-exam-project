from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('conditions/', views.conditions, name='conditions'),
    path('about/', views.about, name='about'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]

