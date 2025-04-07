from django.urls import path
from django.conf import settings
from django.views.static import serve
from . import views
from .views import *

app_name = 'cobros_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-clientes/', views.crear_cliente, name='crear_cliente'),
    path('lista-clientes/', views.lista_clientes, name='lista_clientes'),
    path("clientes/json/", ClientesList.as_view(), name="clientes_json"),

]
