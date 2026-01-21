from django.urls import path
from . import views


urlpatterns = [
    path('movie/', views.MovieListCreateView.as_view(), name='movie-create-list'),
    path('movie/<int:pk>', views.MovieRetriveUpdateDestroyView.as_view(), name='movie-detail-view'),
    path('movie/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]
