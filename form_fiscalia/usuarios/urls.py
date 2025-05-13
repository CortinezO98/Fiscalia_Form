from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('agente/', views.dashboard_agente, name='dashboard_agente'),
    path('supervisor/', views.dashboard_supervisor, name='dashboard_supervisor'),
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('reportes/', views.reportes_view, name='reportes'),

]
