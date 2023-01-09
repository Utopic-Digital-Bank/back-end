from rest_framework import serializers
from launch.serializers import LaunchSerializer
from .models import Invoice
from datetime import date, datetime
import ipdb

class InvoiceSerializer(serializers.ModelSerializer):
    launch = LaunchSerializer(many=True, read_only=True)
    #value = serializers.SerializerMethodField(method_name='sub_total')

    class Meta:
        model = Invoice
        fields = [
            'id', 
            'value', 
            'month_reference', 
            'closing_date',
            'paid',
            'due_date',
            'launch',
        ]
        read_only_fields = [
            'value',
            'due_date', 
            'month_reference',
            'launch',
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
        date_reference = datetime(int(current_year), int(current_month), int(card.due_date))
        closing_date = validated_data.get('closing_date')
        object.closing_date = closing_date
        object.month_reference = str(date_reference.strftime("%Y-%m-%d"))
        object.due_date = str(date_reference.strftime("%Y-%m-%d"))
        object.save()
        return object


    def update(self, instance: Invoice, validated_data: dict) -> Invoice:        
        for key, value in validated_data.items():            
            if key == 'paid':
                if (value is True):
                    setattr(instance, key, value)
                else:
                    raise ValueError(f"It's not possible to change the payment status")
            else:
                raise KeyError(f"The parameter {key} not is alterabled")

    def sub_total(self, obj:Invoice):
        return int(200)