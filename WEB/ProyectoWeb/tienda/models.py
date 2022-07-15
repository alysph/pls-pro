from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from tkinter import CASCADE
from turtle import update
from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

class Genero(models.Model):
    idGenero=models.IntegerField(primary_key=True, verbose_name='ID de Genero')
    nombreGenero=models.CharField(max_length=50,
    verbose_name='Nombre del género')

    def __str__(self):
        return(self.nombreGenero)


class Cliente(models.Model):
    rut = models.CharField(max_length=20, primary_key=True, verbose_name='RUT')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    correo = models.CharField(max_length=30, verbose_name='Correo')
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50, verbose_name='Dirección')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return(self.rut)