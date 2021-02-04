from django.db import models


''' Variable declaradas para un mejor uso en las funciones '''
JA = 'Jamon'
CH = 'Champiñon'
PI = 'Pimentón'
DQ = 'Doble Queso'
AC = 'Aceitunas'
PP = 'Pepperoni'
SA = 'Salchichón'

P = 'Pequeño'
M = 'Mediano'
G = 'Grande'


''' Listas para permitir campos CHOICES '''
INGREDIENTES = [
    (JA, 'Jamon'), 
    (CH, 'Champiñon'), 
    (PI, 'Pimentón'), 
    (DQ, 'Doble Queso'), 
    (AC, 'Aceitunas'), 
    (PP, 'Pepperoni'), 
    (SA, 'Salchichón'),
]

TAMAÑO = [
    (P, 'Pequeño'),
    (M, 'Mediano'),
    (G, 'Grande'),
]

''' Contiene los ingredientes a usar '''
class Ingredientes (models.Model):
    ingrediente = models.CharField(max_length=20, choices=INGREDIENTES)

    def __str__(self):
        return self.ingrediente


''' Almacena los pedidos generados por los clientes
    teniendo asi una variable pizzas donde registrara todas las
    pizzas para cada iteracion de Pedido '''
class Pedido (models.Model):
    fecha = models.DateTimeField('fecha pedido')
    pizzas = models.ManyToManyField('Pizza', through='Pedido_Pizzas', related_name='pizzas')

    def __str__(self):
        return ('Pedido #%s' % self.pk)


''' Almacena los ingredientes, tamaño y precio de la pizza actual '''
class Pizza (models.Model):
    adicionales = models.ManyToManyField('Ingredientes', through='Pizza_Ing', related_name='adicionales')
    costo = models.IntegerField()
    tamaño = models.CharField(max_length=20, choices=TAMAÑO)

    def __str__(self):
        return ('Pizza #%s' % self.pk)


''' Modelos generados manualmente para la correcta comunicacion de
    los ManyToManyField en los modelos anteriores '''
class Pedido_Pizzas (models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

class Pizza_Ing (models.Model):
    ingredientes = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)