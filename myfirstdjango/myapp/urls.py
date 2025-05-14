from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),  # Главная страница
    path('data/', views.data_view, name='data_view'),
    path('test/', views.test_view, name='test_view'),
]
