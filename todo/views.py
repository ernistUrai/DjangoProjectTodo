from rest_framework import viewsets
from .serializers import MovieSerializers

# from django.shortcuts import get_object_or_404
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .forms import MovieForm, MovieCommentForm
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers






# # Create your views here.
# class MovieListView(ListView):
#     template_name = 'movie_list.html'
#     queryset = Movie.objects.all()
#
#     def get_queryset(self):
#         return Movie.objects.all()
#
#
# class MovieDetailView(DetailView):
#     template_name = 'movie_detail.html'
#
#     def get_object(self, **kwargs):
#         movie_id = self.kwargs.get('id')
#         return get_object_or_404(Movie, id=movie_id)
#
# class MovieTooListView(ListView):
#     template_name = 'movie_too_list.html'
#     queryset = Movie.objects.all()
#
#     def get_queryset(self):
#         return Movie.objects.all()
#
#
# class MovieCreateView(CreateView):
#     template_name = 'movie_create.html'
#     form_class = MovieForm
#     queryset = Movie.objects.all()
#     success_url = '/'
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super(MovieCreateView, self).form_valid(form=form)
#
#
# class MovieUpdateView(UpdateView):
#     template_name = 'movie_update.html'
#     form_class = MovieForm
#     success_url = '/'
#
#     def get_object(self, **kwargs):
#         movie_id = self.kwargs.get('id')
#         return get_object_or_404(Movie, id=movie_id)
#
#     def form_valid(self, form):
#         return super(MovieUpdateView, self).form_valid(form=form)
#
# class MovieDeleteView(DeleteView):
#     template_name = 'movie_delete.html'
#     success_url = '/'
#
#     def get_object(self, **kwargs):
#         movie_id = self.kwargs.get('id')
#         return get_object_or_404(Movie, id=movie_id)
#
#
# class MovieCommentView(CreateView):
#     template_name = 'movie_comment.html'
#     form_class = MovieCommentForm
#     queryset = Movie.objects.all()
#     success_url = '/'
#
#     def get_object(self, **kwargs):
#         movie_id = self.kwargs.get('id')
#         return get_object_or_404(MovieCommentForm, id=movie_id)
#
#     def form_valid(self, form):
#         print(form.clean)
#         return super(MovieCommentView,self).form_valid(form=form)