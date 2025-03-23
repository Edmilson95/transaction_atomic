from django.contrib import admin
from .models import Medicamento, Pedido, ItemPedido

admin.site.register(Medicamento)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
