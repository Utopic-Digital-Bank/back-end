from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "balance",
            "created_at",
            "user_id",
        ]
        read_only_fields = ["balance", "created_at","balance","user_id"]


class UpdateAccount(serializers.ModelSerializer):
    model = Account
    fields = [
        "insurance_id",
        "economic_consultance_id"
    ]
