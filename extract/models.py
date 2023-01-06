from django.db import models

class OperationOptions(models.TextChoices):
    SAIDA = ["pix", "transferência", "saque", "pagamento"]
    ENTRADA = ["depósito"]
    ERRO = "NÃO EFETUADO"

class Extract(models.Model):
    
    # Detalhes do faturamento(Valor anterior e Valor atual)
    valueOperation = models.FloatField(max_length=17, default= 00.1)
    previous_balance = models.FloatField(max_length=17)
    current_balance = models.FloatField(max_length=17)

    # Referencias do Faturamento(Tipo de Operação, Data Criação e Chave Estrangeira da 'conta')
    operation = models.CharField(max_length=12, choices=OperationOptions.choices, default=OperationOptions.ERRO)
    created_at = models.DateTimeField()
    account = models.ForeignKey("account.Account", related_name="extract", on_delete=models.PROTECT)
