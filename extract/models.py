from django.db import models


class Extract(models.Model):
    # Detalhes do faturamento(Valor anterior e Valor atual)
    previous_balance = models.FloatField(max_length=17)
    current_balance = models.FloatField(max_length=17)

    # Referencias do Faturamento(Tipo de Operação, Data Criação e Chave Estrangeira da 'conta')
    operation = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    account = models.ForeignKey("account.Account", related_name="extract", on_delete=models.PROTECT)
