from django.db import models

class OperationOptions(models.TextChoices):
    PIX = "pix",
    TRANSFERÊNCIA = "transferência", 
    SAQUE = "saque",
    PAGAMENTO = "pagamento"
    DEPÓSITO = "depósito"

class Extract(models.Model):
    
    # Detalhes do faturamento(Valor anterior e Valor atual)
    valueOperation = models.FloatField(max_length=17, default= 00.1)
    previous_balance = models.FloatField(max_length=17)
    current_balance = models.FloatField(max_length=17)

    # Referencias do Faturamento(Tipo de Operação, Data Criação e Chave Estrangeira da 'conta')
    operation = models.CharField(max_length=13, choices=OperationOptions.choices)
    created_at = models.DateTimeField()
    account = models.ForeignKey("account.Account", related_name="extract", on_delete=models.PROTECT)
