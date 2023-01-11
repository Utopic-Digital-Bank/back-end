from rest_framework import serializers
from launch.serializers import LaunchSerializer
from .models import Invoice
from datetime import date, datetime
import ipdb
from django.shortcuts import get_object_or_404
from account.models import Account
from card.models import Card



class InvoiceSerializer(serializers.ModelSerializer):
    launch = LaunchSerializer(many=True, read_only=True)
    # value = serializers.SerializerMethodField(method_name='sub_total')

    class Meta:
        model = Invoice
        fields = [
            'id',
            'value',
            'closing_date',
            'paid',
            'due_date',
            'launch',
            'card',
        ]
        read_only_fields = [
            'value',
            'due_date',
            'launch',
            'card',
        ]

    def create(self, validated_data):
        card = validated_data['card']
        object = Invoice()
        object.card_id = card.id

        current_date = date.today()
        current_day = current_date.strftime('%d')
        current_month = current_date.strftime('%m')
        current_year = current_date.strftime('%Y')

        if int(current_day) >= int(card.due_date):
            if int(current_month) == 12:
                current_year = int(current_year) + 1
                current_month = 1
            current_month = int(current_month) + 1
        date_reference = datetime(int(current_year), int(
            current_month), int(card.due_date))
        closing_date = validated_data.get('closing_date')
        object.closing_date = closing_date
        object.month_reference = str(date_reference.strftime("%Y-%m-%d"))
        object.due_date = str(date_reference.strftime("%Y-%m-%d"))
        object.save()
        return object

    def update(self, instance: Invoice, validated_data: dict) -> Invoice:
        for key, value in validated_data.items():
            if key == 'paid':
                if value == True:
                    setattr(instance, key, value)
                else:
                    raise ValueError(
                        f"It's not possible to change the payment status")
            else:
                raise KeyError(f"The parameter {key} not is alterabled")
            #ipdb.set_trace()
            card = get_object_or_404(Card, id=self.data['card'])
            account = get_object_or_404(Account, id=card.account_id)
            #ipdb.set_trace()
            #if instance.paid == True:
                #raise serializers.ValidationError({"validationError": "It's not possible to change the payment status"})
            #ipdb.set_trace()
            if account.balance >= self.data['value']:
                account.balance -= self.data['value']
                instance.paid = True
                instance.save()
                account.save()
            else:
                raise serializers.ValidationError({"balanceError": "Balance of account insufficient"})
        return instance

    def sub_total(self, obj: Invoice):
        return sum(obj.value)