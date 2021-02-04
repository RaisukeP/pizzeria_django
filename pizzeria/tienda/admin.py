from django.contrib import admin
from .models import Pedido, Pizza, Ingredientes
from rangefilter.filter import DateRangeFilter

class IngredientesUsadosFilter(admin.SimpleListFilter):
    title = 'ingredientes_usados'
    parameter_name = 'ingredientes_usados'

    def lookups(self, request, model_admin):
        return [
            ('Jamon', 'Jamon'), 
            ('Champiñon', 'Champiñon'), 
            ('Pimentón', 'Pimentón'), 
            ('Doble Queso', 'Doble Queso'), 
            ('Aceitunas', 'Aceitunas'), 
            ('Pepperoni', 'Pepperoni'), 
            ('Salchichón', 'Salchichón'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Pimenton':
            return queryset.filter(pizzas__adicionales='Pimenton')
        elif value == 'No':
            return queryset.exclude(ingredientes_usados__gt=75)
        return queryset

''' Muestra el apartado de las pizzas a causa del ManytoManyField '''
class PedidoInline(admin.StackedInline):
    model = Pedido.pizzas.through

''' Actualizando la pantalla de Pedido en la seccion principal y de agregar/eliminar '''
class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    list_display = ('__str__', 'pizzas_ordenadas','ingredientes_usados', 'fecha')
    list_filter = (('fecha',DateRangeFilter),IngredientesUsadosFilter)
    
    inlines = [
        PedidoInline,
    ]

    ''' Busca que pizzas fueron ordenadas en ese pedido '''
    def pizzas_ordenadas(self, obj):
        return [a for a in obj.pizzas.all()]

    ''' Busca y guarda todos los ingredientes para el objeto de Pedido correspondiente '''
    def ingredientes_usados(self, obj):
        resultado = []
        for b in obj.pizzas.all():
            for a in b.adicionales.all():
                resultado.append(a)
        return resultado

''' Muestra el apartado de las pizzas a causa del ManytoManyField '''
class PizzaInline(admin.StackedInline):
    model = Pizza.adicionales.through

''' Actualizando la pantalla de Pizza en la seccion principal y de agregar/eliminar '''
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('__str__','tamaño', 'costo', 'muestra_ingredientes')
    inlines = [
        PizzaInline,
    ]

    def muestra_ingredientes(self, obj):
        return [a for a in obj.adicionales.all()]

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Ingredientes)