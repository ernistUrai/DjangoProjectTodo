from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField("Название фильма",  max_length=100, help_text="Максимум 100 символов")
    genres = models.CharField("Жанр", max_length=50, help_text="Максимум 50 символов")
    director = models.CharField("Режиссер", max_length=50, help_text="Максимум 50 символов", null=True)
    description = models.TextField("Коротко о фильме")
    image = models.ImageField("Фотография о фильме" , upload_to="")
    video = models.URLField("Фильм")
    duration = models.CharField( "Продолжительность", max_length=50, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title