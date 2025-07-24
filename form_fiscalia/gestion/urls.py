from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_evaluacion/', views.crear_evaluacion, name='crear_evaluacion'),
    path('buscar/', views.buscar_tipificacion, name='buscar_tipificacion'),
    path('reportes/', views.reportes_view, name='reportes'),
    path('reportes/exportar_excel/', views.exportar_excel, name='exportar_excel'),

    # APIs Nuevas - Nueva jerarquía
    path('api/tipos-canal/', api.tipos_canal, name='tipos_canal'),
    path('api/segmentos/', api.segmentos, name='segmentos'),
    path('api/segmentos-ii/', api.segmentos_ii, name='segmentos_ii'),
    path('api/tipificaciones/', api.tipificaciones, name='tipificaciones'),
    path('api/categorias/', api.categorias, name='categorias'),
    path('api/subcategorias/', api.subcategorias, name='subcategorias'),
    
    # APIs para mantener compatibilidad
    path('api/tipificaciones-old/', api.tipificaciones_old, name='tipificaciones_old'),
    path('api/categorias-old/', api.categorias_old, name='categorias_old'),
    
    # API existente
    path('api/ciudadano/', api.ciudadano, name='ciudadano'),
]