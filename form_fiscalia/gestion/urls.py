from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_evaluacion/', views.crear_evaluacion, name='crear_evaluacion'),
    path('buscar/', views.buscar_tipificacion, name='buscar_tipificacion'),
    path('reportes/', views.reportes_view, name='reportes'),
    path('reportes/exportar/', views.exportar_csv, name='exportar_csv'),

    # Endpoints API
    path('api/ciudadano/', api.ciudadano, name='ciudadano'),
    path('api/tipificaciones/', api.tipificaciones, name='tipificaciones'),
    path('api/categorias/', api.categorias, name='categorias'),
    path('api/subcategorias/', api.subcategorias, name='subcategorias'),
]