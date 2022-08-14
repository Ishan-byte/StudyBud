from django.urls import path 
from . import views

urlpatterns = [
    path('', views.getroutes ),
    path('rooms/', views.getrooms),
    path('room/<str:pk>', views.getroom)
]