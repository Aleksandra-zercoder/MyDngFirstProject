from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model  = Film
        fields = ['title', 'description', 'review', 'genre', 'year', 'country']
        widgets = {
            'title':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Краткое описание'}),
            'review':      forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ваш отзыв'}),
            'genre':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Жанр'}),
            'year':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Год выпуска'}),
            'country':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Страна'}),
        }
