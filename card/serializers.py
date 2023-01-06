from rest_framework import serializers

from .models import Card, DueDateChoices, CardChoices

from invoices.models import Invoice
from account.models import Account

import datetime
import random
class CardSerializer(serializers.Serializer):
    number = serializers.SerializerMethodField()
    password= serializers.CharField()
    cvv = serializers.SerializerMethodField()
    balance_invoices= serializers.SerializerMethodField()
    due_date= serializers.ChoiceField(choices= DueDateChoices.choices, default= DueDateChoices.first_option)
    due_card= serializers.SerializerMethodField()
    type = serializers.ChoiceField(choices= CardChoices.choices, default= CardChoices.debit)
    total_limit = serializers.SerializerMethodField()
    available_limit = serializers.SerializerMethodField()
    is_active= serializers.BooleanField(read_only=True)

    def get_number(self, obj):
        number = random.randomint(1000000000000000,9999999999999999)
        numberAlreadyExists= Card.objects.get(number=number)
        if numberAlreadyExists:
            number = random.randomint(1000000000000000,9999999999999999)
        return str(number)
    
    def get_cvv(self, obj):
        cvv = random(100,999)
        cvv_already_exists= Card.objects.get(cvv=cvv)
        if cvv_already_exists:
            cvv = random(100,999)
        return cvv

    def get_balance_invoices(self, obj):
        invoice_balance= Invoice.objects.get(card_id= self.id)
        if invoice_balance:
            return invoice_balance
        return 0

    def get_due_card(self, obj):
        date_now = datetime.datetime.now()
        year= date_now.year
        return f"{date_now.month}/{year+4}"

    def get_total_limit(self,obj):
        if self.type == "Crédito":
            balance =  Account.objects.get(account_id=self.account_id)
            return balance.balance * 3
        return 0

    def get_available_limit(self,obj):
        available_limit= self.total_limit - self.balance_invoices
        return available_limit

    def create(self, validated_data):
        card= Card.objects.create(**validated_data)
        return card
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if (key is "due_date"):
                setattr(instance, key, value)

            else:
                raise KeyError(f"The parameter {key} not is alterabled")

        instance.save()

        return instance



