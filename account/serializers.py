from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "balance",
            "created_at",

            "user_id"
        ]
        read_only_fields = [ "id",
            "balance",
            "created_at",
            "user_id"]



class UpdateAccount(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
        "insurance_id",
        "economic_consultance_id",
        "id",
        "balance",
        "created_at",
        "user_id"
        ]
        read_only_fields = [ "id",
            "balance",
            "created_at",
            "user_id"]
