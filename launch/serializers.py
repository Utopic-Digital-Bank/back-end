from rest_framework import serializers
from .models import Launch


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = [
            "id",
            "value",
            "establishment",
            "date_hour",
        ]

    def create(self, validated_data):
        launch = Launch.objects.create(
            **validated_data,
        )

        return launch
