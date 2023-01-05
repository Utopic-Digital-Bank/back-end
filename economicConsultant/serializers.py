from rest_framework import serializers
from .models import EconomicConsultant


class EconomicConsultantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

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
