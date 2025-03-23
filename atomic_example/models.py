from django.db import models

class Medicamento(models.Model):
    nome = models.CharField(max_length=30)
    estoque = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)
    #through indica a tabela para controlar a relação do models Pedido e Medicamento
    #usamos o throuh em pedido pq é o pedido que 'contem' medicamentos.
    medicamentos = models.ManyToManyField(Medicamento, through='ItemPedido')
    pagamento_confirmado = models.BooleanField(default=False) # False não pago, True pago
       
    def __str__(self):
        return f"Id Pedido: {self.pk}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Pedido ID: ´´{self.pedido.pk}´´ - Medicamento: ´´{self.medicamento}´´ - Qtd: ´´{self.quantidade}´´"
    
    