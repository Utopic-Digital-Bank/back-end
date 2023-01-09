from django.db import models


class OperationOptions(models.TextChoices):
    PIX = "pix",
    TRANSFERÊNCIA = "transferência",
    SAQUE = "saque",
    PAGAMENTO = "pagamento"
    DEPÓSITO = "depósito"


class Extract(models.Model):

    # Detalhes do faturamento(Valor anterior e Valor atual)
    valueOperation = models.DecimalField(max_digits=17, decimal_places=2)
    previous_balance = models.DecimalField(max_digits=17, decimal_places=2)
    current_balance = models.DecimalField(max_digits=17, decimal_places=2)

    # Referencias do Faturamento(Tipo de Operação, Data Criação e Chave Estrangeira da 'conta')
    operation = models.CharField(
        max_length=13, choices=OperationOptions.choices)
    creation_date = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(
        "account.Account", related_name="extract", on_delete=models.PROTECT)
