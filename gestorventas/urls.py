from django.urls import path
from . import views

app_name = 'gestorventas'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_venta, name='registrar_venta'),
    path('calcular-bono/', views.calcular_bono, name='calcular_bono'),
]