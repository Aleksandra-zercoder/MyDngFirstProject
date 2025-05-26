from django.urls import path
from . import views

urlpatterns = [
    path('add/',   views.film_create, name='film_create'),
    path('',      views.film_list,   name='film_list'),
]
