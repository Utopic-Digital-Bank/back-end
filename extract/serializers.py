from rest_framework import serializers
from .models import Extract, OperationOptions
from account.models import Account
from django.shortcuts import *
import ipdb


class ExtractSerializer(serializers.ModelSerializer):
    operation = serializers.ChoiceField(choices=OperationOptions.choices)

    class Meta:
        model = Extract
        fields = [
            "valueOperation",
            "previous_balance",
            "current_balance",
            "operation",
            "creation_date",
            "account_id",
        ]
        read_only_fields = ["previous_balance",
                            "current_balance"]

    def create(self, validated_data):
        account = get_object_or_404(Account, id=validated_data["account_id"])
        valueOperation = validated_data["valueOperation"]
        validated_data["previous_balance"] = account.balance

        if validated_data["operation"] == "depósito":
            validated_data["current_balance"] = (float(valueOperation) +
                                                 float(validated_data["previous_balance"]))
            account.balance = validated_data["current_balance"]
        else:
            validated_data["current_balance"] = (
                float(validated_data["previous_balance"]) - float(valueOperation))
            account.balance = validated_data["current_balance"]

        account.save()
        return Extract.objects.create(**validated_data)
