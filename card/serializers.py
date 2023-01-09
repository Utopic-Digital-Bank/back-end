from rest_framework import serializers

from .models import Card, DueDateChoices, CardChoices


class CardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    password= serializers.CharField()
    cvv = serializers.CharField(read_only=True)
    balance_invoices= serializers.FloatField(read_only=True)
    due_date= serializers.ChoiceField(choices= DueDateChoices.choices, default= DueDateChoices.first_option)
    due_card= serializers.CharField(read_only=True)
    type = serializers.ChoiceField(choices= CardChoices.choices, default= CardChoices.debit)
    total_limit = serializers.FloatField(read_only=True)
    available_limit = serializers.FloatField(read_only=True)
    is_active= serializers.BooleanField(read_only=True)


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



