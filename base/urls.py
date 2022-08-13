from django.urls import path
from . import views

urlpatterns = [
    # User
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logOutUser, name="logout"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('edit-profile/<str:pk>/', views.editUserProfile, name="edit-profile"),

    # Home
    path('', views.home, name="home"),

    # Rooms
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),

    # Messages
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    # Mobile
    path('topics/', views.topicsPage, name="topics-page"),
    path('activities/', views.activitiesPage, name="activities-page")
]
