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

    def delete(self):
        self.is_active = False
        self.save()
