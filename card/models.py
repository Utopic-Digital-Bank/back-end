from django.db import models


class CardChoices(models.TextChoices):
    debit = "Debit"
    credit = "Credit"
    both = "Múltiplo"


class DueDateChoices(models.TextChoices):
    first_option = "05"
    second_option = "15"
    third_option = "29"


class Card(models.Model):
    # Dados de segurança(Número do Cartão, Senha e CVV)
    number = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    cvv = models.CharField(max_length=3)

    # Dados da Fatura(Valor Atual, Dia do Vencimento, Tipo do Cartão)
    balance_invoices = models.FloatField(max_length=17)
    due_date = models.CharField(
        max_length=8,
        choices=DueDateChoices.choices,
        default=DueDateChoices.first_option
    )
    due_card = models.CharField(max_length=8)
    type = models.CharField(
        max_length=8,
        choices=CardChoices.choices,
        default=CardChoices.debit,
    )

    # Detalhamento da Fatura(Limite Total, Limite Disponivel, Data do Vencimento)
    total_limit = models.FloatField(max_length=17)
    available_limit = models.FloatField(max_length=17)

    # Detalhamento do status do cartão(Status atual, Chave Estrangeira do app 'Conta' )
    is_active = models.BooleanField(default=True)
    account = models.ForeignKey(
        "account.Account", related_name="card", on_delete=models.PROTECT)
