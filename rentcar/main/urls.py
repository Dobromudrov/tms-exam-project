from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('cars/', CarsPage.as_view(), name='cars'),
    path('conditions/', ConditionsPage.as_view(), name='conditions'),
    path('contacts/', ContactsPage.as_view(), name='contacts'),
    path('add_cars/', AddCars.as_view(), name='add_cars'),
    path('cars/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('cars/<slug:post_slug>/order', PostOrder.as_view(), name='order'),
    path('cars/<slug:post_slug>/update/', UpdatePost.as_view(), name='post-update'),
    path('cars/<slug:post_slug>/delete/', DeletePost.as_view(), name='post-delete'),
    path('category/<slug:cat_slug>/', CarsCategory.as_view(), name='category'),
    path('application/', Application.as_view(), name='application'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('feedback_list/', FeedbackList.as_view(), name='feedback_list'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
