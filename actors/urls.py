from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorListCreateAPIView.as_view(), name='actor-create-list'),
    path('actor/<int:pk>', views.ActorRetriveUpdateDestroyAPIView.as_view(), name='actor-detail-view'),
]
