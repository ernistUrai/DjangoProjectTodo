from rest_framework import routers
from django.urls import path, include
# from . import views
# from ..todo_project.urls import urlpatterns
from .views import MovieViewSet

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('', views.MovieListView.as_view(), name="movie_list"),
#     path('movie_too_list/', views.MovieTooListView.as_view(), name="movie_too_list"),
#     path('movie_list/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
#     path('movie_create/', views.MovieCreateView.as_view(), name='movie_create'),
#     path('movie_too_list/<int:id>/movie_update/', views.MovieUpdateView.as_view(), name='movie_update'),
#     path('movie_too_list/<int:id>/movie_delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
#     path('movie_detail/<int:id>/movie_comment/', views.MovieCommentView.as_view(), name="car_comment"),
#
# ]