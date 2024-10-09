from django import forms
from .models import Movie
from django.forms import TextInput


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

        # widgets = {
        #     'title': TextInput(attrs={
        #     'class': 'control',
        #     'placeholder': 'Название фильма'
        # }),
        #     'genres': TextInput(attrs={
        #         'class': 'control',
        #         'placeholder': 'Жанр'
        #     }),
        #     'director': TextInput(attrs={
        #         'class': 'control',
        #         'title': TextInput(attrs={
        #             'class': 'control',
        #         }),
        #         'placeholder': 'Режиссер'
        #     }),
        #     'description': TextInput(attrs={
        #         'class': 'control',
        #         'placeholder': 'Коротко о фильме'
        #     }),
        #     'image': TextInput(attrs={
        #         'class': 'control',
        #         'placeholder': 'Фотография о фильме'
        #     }),
        #     'video': TextInput(attrs={
        #         'class': 'control',
        #         'placeholder': 'Ссылка  фильма'
        #     }),
        #     'duration': TextInput(attrs={
        #         'class': 'control',
        #         'placeholder': 'Продолжительность'
        #     }),
        # }
        #
