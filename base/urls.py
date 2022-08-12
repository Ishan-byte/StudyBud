from django.urls import path
from . import views

urlpatterns = [
    # User
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logOutUser, name="logout"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    # Home
    path('', views.home, name="home"),

    # Rooms
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),

    # Messages
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

]
