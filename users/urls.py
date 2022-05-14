from django.contrib import admin
from django.urls import path, include
from .views import LoginView, LogoutView, ProfileView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', ProfileView.as_view()),
    path('logout', LogoutView.as_view()),
    
]