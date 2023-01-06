from rest_framework import serializers
from .models import InvestmentCdi


class InvestmentCdiSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = InvestmentCdi

        fields = [
            "id",
            "initial_value",
            "current_value",
            "yield_value",
            "creation_date",
            "account"
        ]

    def create(self, validated_data):
        investmentCdi = InvestmentCdi.objects.create(**validated_data)

        return investmentCdi


class GetAllInvestmentCdiSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentCdi

        fields = [
            "id",
            "current_value"
        ]
