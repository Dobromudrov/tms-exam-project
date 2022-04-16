from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('cars/', CarsPage.as_view(), name='cars'),
    path('conditions/', ConditionsPage.as_view(), name='conditions'),
    path('about/', AboutPage.as_view(), name='about'),
    path('add_cars/', AddCars.as_view(), name='add_cars'),
    path('cars/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarsCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
