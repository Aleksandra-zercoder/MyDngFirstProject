from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News(models.Model):
    title           = models.CharField("Заголовок", max_length=200)
    description     = models.CharField("Краткое описание", max_length=500)
    content         = models.TextField("Текст новости")
    pub_date        = models.DateTimeField("Время публикации", auto_now_add=True)
    author          = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        related_name='news'
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
