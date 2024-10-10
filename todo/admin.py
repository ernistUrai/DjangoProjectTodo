from django.contrib import admin
from .models import Movie, MovieCommentModels


# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieCommentModels)
