from rest_framework import serializers
from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = [
            'id', 
            'value', 
            'month', 
            'paid',
            'due_date',
        ]

    def update(self, instance: Invoice, validated_data: dict) -> Invoice:        
        for key, value in validated_data.items():            
            if (key is 'paid'):
                if (value is True):
                    setattr(instance, key, value)
                else:
                    raise ValueError(f"It's not possible to change the payment status")
            else:
                raise KeyError(f"The parameter {key} not is alterabled")