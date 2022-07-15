from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "ProyectoWebApp/index.html")

def galeria(request):
        return render(request, "ProyectoWebApp/galeria.html")