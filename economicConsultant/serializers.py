from rest_framework import serializers
from .models import EconomicConsultant


class EconomicConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicConsultant

        fields = [
            "id",
            "name",
            "specialty",
        ]

    def create(self, validated_data):
        economicConsultant = EconomicConsultant.objects.create(
            **validated_data)

        return economicConsultant


class GetEconomicConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicConsultant

        fields = [
            "id",
            "name",
            "specialty",
        ]

    read_only_fields = ["specialty"]
