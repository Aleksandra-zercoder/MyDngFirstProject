from django.contrib import admin
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title',)
from django.contrib import admin

# Register your models here.
