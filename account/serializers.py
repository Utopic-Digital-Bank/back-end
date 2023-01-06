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
            "insurance_id",
            "economic_consultance_id",
        ]
        extra_kwargs = {["balance","created_at"]: {"read_only": True}}


class UpdateBalance(serializers.ModelSerializer):
    model = Account
    fields = [
        "balance"
        ]