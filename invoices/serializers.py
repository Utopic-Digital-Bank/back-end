from rest_framework import serializers
from .models import Invoice
import ipdb
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = [
            'id', 
            'value', 
            'month_reference', 
            'closing_date',
            'paid',
            'due_date',
        ]
        read_only_fields = [
            'id', 
            'closing_date', 
            'due_date', 
            'month_reference', 
            'value',
        ]
    
    def create(self, validated_data):
        card = validated_data['card']
        objeto = Invoice()
        data = timedelta(days=int(card.due_date))
        due_days = int(card.due_date)
        objeto.value = 400.00
        objeto.card_id = 1
        current_date = date.today()
        current_day = current_date.strftime('%d')
        current_month = current_date.strftime('%m')
        current_year = current_date.strftime('%Y')
        
        if int(current_day) >= int(card.due_date):
            if int(current_month) == 12:
                current_year = int(current_year) + 1
                current_month = 1
            current_month = int(current_month) + 1
        date_reference = datetime(int(current_year), int(current_month), int(card.due_date))
        closing_date = datetime(int(current_year), int(current_month), (int(card.due_date)-5))
        objeto.closing_date = closing_date.strftime("%Y-%m-%d")
        objeto.month_reference = str(date_reference.strftime("%Y-%m-%d"))
        objeto.due_date = str(date_reference.strftime("%Y-%m-%d"))
        objeto.save()
        return objeto

    def update(self, instance: Invoice, validated_data: dict) -> Invoice:        
        for key, value in validated_data.items():            
            if key == 'paid':
                if (value is True):
                    setattr(instance, key, value)
                else:
                    raise ValueError(f"It's not possible to change the payment status")
            else:
                raise KeyError(f"The parameter {key} not is alterabled")