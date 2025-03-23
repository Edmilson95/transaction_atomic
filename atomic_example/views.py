from django.http import HttpResponse
from .models import *
from django.db import transaction


#@transaction.atomic na assinatura do método
def pedidos(request):
    
    with transaction.atomic():
        dipirona = Medicamento.objects.create(nome="dipirona", estoque=30)
        dorflex = Medicamento.objects.create(nome="dorflex", estoque=30)
        
        
        pedido = Pedido.objects.create(pagamento_confirmado=False)
        
        pedido_id = pedido.id # acessando id do pedido recem criado
        
        if pedido.pagamento_confirmado == False:
            raise ValueError(f"Pagamento do pedido id ->'{pedido_id}'<- não processado")
            
        # Cria a relação medicamento/pedido com quantidade 
        ItemPedido.objects.create(medicamento=dipirona, pedido=pedido, quantidade=10)
        ItemPedido.objects.create(medicamento=dorflex, pedido=pedido, quantidade=10)
        
        return HttpResponse("Testando transaction.atomic")
