from django.db import models

class Film(models.Model):
    title       = models.CharField("Название",    max_length=200)
    description = models.TextField("Описание")
    review      = models.TextField("Отзыв")
    genre       = models.CharField("Жанр",        max_length=100, default="", blank=True)
    year        = models.PositiveIntegerField("Год выпуска", default=2025)
    country     = models.CharField("Страна",      max_length=100, default="", blank=True)

    def __str__(self):
        return self.title

