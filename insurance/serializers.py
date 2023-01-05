from rest_framework import serializers
from .models import Insurance


class InsuranceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

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
            if (key is 'tuition'):
                setattr(instance, key, value)

            else:
                raise KeyError(f"The parameter {key} not is alterabled")

        instance.save()

        return instance
