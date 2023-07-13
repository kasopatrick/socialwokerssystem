from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('conduct/', views.conduct, name='conduct'),
    path('membership/', views.membership, name='membership'),
    path('development/', views.development, name='development'),
    path('advocacy/', views.advocacy, name='advocacy'),
    path('resources/', views.resources, name='resources'),






]