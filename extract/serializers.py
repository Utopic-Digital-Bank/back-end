from rest_framework import serializers
from .models import Extract


class ExtractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extract
        fields = '__all__'
