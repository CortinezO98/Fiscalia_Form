from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('buscar/', views.buscar_tipificaciones, name='buscar_tipificaciones'),
    # path('exportar/', views.exportar_csv, name='exportar_csv'),
]