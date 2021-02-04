from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Pedido

def pedido (request):
    ultimo_pedido = Pedido.objects.last()
    resultado = ultimo_pedido.pizzas.all()
    output = resultado.values()
    return HttpResponse(output)