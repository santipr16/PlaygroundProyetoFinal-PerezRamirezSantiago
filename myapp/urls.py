from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path('listado_alumnos/', views.listado_alumnos, name='listado_alumnos'),
    path('listado_profesores/', views.listado_profesores, name='listado_profesores'),
    path('listado_instrumentos/', views.listado_instrumentos, name='listado_instrumentos'),
    path('agregar_instrumento/', views.agregar_instrumento, name='agregar_instrumento'),
    path('agregar_foto/', views.agregar_foto, name='agregar_foto'),
    path('logout/', views.logout, name='logout'),
    path('fotos/', views.foto, name='fotos'),
    path('login/index/', views.index, name='index'),
    path('', include('login.urls')),

]