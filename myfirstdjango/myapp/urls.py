from django.urls import path
from . import views

urlpatterns = [
    path('',      views.home_view,  name='home_view'),
    path('data/', views.data_view,  name='data_view'),
    path('test/', views.test_view,  name='test_view'),
    path('about/',views.about_view, name='about_view'),
]
