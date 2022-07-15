from itertools import product
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from .models import Producto
from .forms import ProductoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def tienda(request):
        productos=Producto.objects.all()
        return render(request, "tienda/tienda.html", {"productos":productos})


@permission_required('tienda.add_producto')
def agregarp(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarp")
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, "tienda/agregarp.html", data)

@permission_required('Mascotas.view_producto')
def listarp(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data ={
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'tienda/listarp.html', data)

@permission_required('tienda.change_producto')
def modificarp(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarp")
        data["form"] = formulario
    return render(request, 'tienda/modificarp.html', data)

@permission_required('tienda.delete_producto')
def eliminarp(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listarp")

from django.shortcuts import render, HttpResponse
from .forms import  ClienteForm
from django.core.paginator import Paginator
from django.http import Http404
from .models import Cliente
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render, get_object_or_404
# Create your views here.

@permission_required('tienda.add_cliente')
def agregarc(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarc")
            data["mensaje"] = "Agregado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'tienda/agregarc.html', data)

@permission_required('tienda.view_cliente')
def listarc(request):
    clientes = Cliente.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(clientes, 5)
        clientes = paginator.page(page)
    except:
        raise Http404

    data ={
        'entity': clientes,
        'paginator': paginator
    }
    return render(request, 'tienda/listarc.html', data)

@permission_required('tienda.change_cliente')
def modificarc(request, rut):
    cliente = get_object_or_404(Cliente, rut=rut)

    data = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarc")
        data["form"] = formulario
    return render(request, 'tienda/modificarc.html', data)

@permission_required('tienda.delete_cliente')
def eliminarc(request, rut):
    rut = get_object_or_404(Cliente, rut=rut)
    rut.delete()
    return redirect(to="listarc")


#Serializers API
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ClienteSerializer

@csrf_exempt
@api_view(['GET', 'POST'])

def listar_clientes(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)