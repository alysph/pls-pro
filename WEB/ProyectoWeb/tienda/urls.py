from django.urls import path
from .views import listar_clientes, agregarp, listarp, modificarp, eliminarp, agregarc, listarc, modificarc, eliminarc
from . import views

#localhost:8000/listar_clientes
urlpatterns = [
    path('', views.tienda, name="tienda"),
    path('agregarp', views.agregarp, name="agregarp"),
    path('listarp', views.listarp, name="listarp"),
    path('modificarp/<id>/', views.modificarp, name="modificarp"),
    path('eliminarp/<id>/', views.eliminarp, name="eliminarp"),
    path('agregarc', views.agregarc, name="agregarc"),
    path('listarc', views.listarc, name="listarc"),
    path('modificarc/<rut>/', views.modificarc, name="modificarc"),
    path('eliminarc/<rut>/', views.eliminarc, name="eliminarc"),
    path('listar_clientes', listar_clientes, name="listar_clientes"),

]