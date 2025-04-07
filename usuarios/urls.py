from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import *

from Cobros_app.urls import app_name
from . import views

app_name = 'usuarios_app'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('change_password/<int:user_id>/', views.change_password, name='change_password'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='usuarios_app:login'), name='logout'),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path("usuarios/json/", UsuariosList.as_view(), name="usuarios_json"),
    path('usuarios/toggle/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),

]
