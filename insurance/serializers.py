from rest_framework import serializers
from .models import Insurance


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance

        fields = [
            "id",
            "name",
            "tuition",
            "is_active"
        ]

    def create(self, validated_data):
        insurance = Insurance.objects.create(**validated_data)

        return insurance

    def update(self, instance: Insurance, validated_data: dict) -> Insurance:
        for key, value in validated_data.items():
            if (key == 'tuition'):
                setattr(instance, key, value)
        instance.save()

        return instance
