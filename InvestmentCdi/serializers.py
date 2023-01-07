from rest_framework import serializers
from .models import InvestmentCdi
from datetime import date
import requests
import json
import ipdb


class InvestmentCdiSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateField(required=False)

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

        read_only_fields = ['id', 'current_value',
                            'yield_value', 'creation_date', 'account',]

    def create(self, validated_data):
        data_fim = date.today()
        data_fim = data_fim.strftime("%Y-%m-%d")
        data_inicio = data_fim
        value = validated_data.get("initial_value")
        value = float(value)
        url = f"https://calculadorarendafixa.com.br/calculadora/di/calculo?dataInicio={data_inicio}&dataFim={data_fim}&percentual=100.00&valor={value}"

        response_b3 = requests.get(url)
        response_b3 = json.loads(response_b3.content)
        validated_data["current_value"] = float(
            response_b3["valorCalculado"])
        validated_data["yield_value"] = (
            float(response_b3["valorCalculado"]) - float(response_b3["valorBase"]))
        return InvestmentCdi.objects.create(**validated_data)


class GetAllInvestmentCdiSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentCdi

        fields = [
            "id",
            "current_value"
        ]
