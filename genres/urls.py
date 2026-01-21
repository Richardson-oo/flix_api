from django.urls import path
from . import views


urlpatterns = [
    path('genre/', views.GenreListCreateAPIView.as_view(), name='genre-create-list'),
    path('genre/<int:pk>', views.GenreRetriveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
