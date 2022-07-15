from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

from .models import Cliente




class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
    
        widget = {
        "fecha": forms.SelectDateWidget()
    }