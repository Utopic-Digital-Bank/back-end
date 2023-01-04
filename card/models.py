from django.db import models

class CardChoices(models.TextChoices):
    debit= "Debit"
    credit= "Credit"
    both= "Múltiplo"


class Card(models.Model):
    # Dados de segurança(Número do Cartão, Senha e CVV)
    number = models.IntegerField(max_length=16)
    password = models.IntegerField(max_length=4)
    cvv = models.IntegerField(max_length=3)

    # Dados da Fatura(Valor Atual, Dia do Vencimento, Tipo do Cartão)
    balance_invoices= models.FloatField(max_length=17)
    due_date = models.IntegerField(max_length=2)
    type = models.CharField(
        max_length=6,
        choices=CardChoices.choices,
        default=CardChoices.debit,
    )

    # Detalhamento da Fatura(Limite Total, Limite Disponivel, Data do Vencimento)
    total_limit = models.FloatField(max_length=17)
    available_limit = models.FloatField(max_length=17)
    card_expiration = models.DateField()

    # Detalhamento do status do cartão(Status atual, Chave Estrangeira do app 'Conta' )
    is_active = models.BooleanField()
    # accountID = models.ForeignKey()
