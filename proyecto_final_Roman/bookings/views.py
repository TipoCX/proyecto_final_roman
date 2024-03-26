from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva

# Create your views here.

def home_view(request):
    return HttpResponse("<h1>lol</h1>")

def create_view(request, nombre_de_usuario, destino):

    # reserva = Reserva("",nombre_de_usuario, destino)
    reserva = Reserva.objects.create(nombre_de_usuario=nombre_de_usuario, destino=destino)
    return HttpResponse(reserva)
