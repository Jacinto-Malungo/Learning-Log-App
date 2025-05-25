from django.urls import path
from django.contrib.auth.views import LoginView
from .views import logout_view

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', 
         LoginView.as_view(
             template_name='users/login.html',
             extra_context={'next': '/'}
         ), 
         name='login'),
    path('logout/', logout_view, name='logout'),

    # Página de cadastro
    path('register/', views.register, name='register'),
]