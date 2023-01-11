from rest_framework import serializers
from .models import Account
from django.shortcuts import get_object_or_404
from insurance.models import Insurance
from economicConsultant.models import EconomicConsultant
from economicConsultant.serializers import GetEconomicConsultantSerializer
from insurance.serializers import GetInsuranceSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "balance",
            "created_at",
            "user_id"
        ]
        read_only_fields = ["id",
                            "balance",
                            "created_at",
                            "user_id"]


class UpdateAccount(serializers.ModelSerializer):
    insurance = GetInsuranceSerializer(many=True, required=False)
    economic_consultance = GetEconomicConsultantSerializer(required=False)

    class Meta:
        model = Account
        fields = [
            "insurance",
            "economic_consultance",
            "id",
            "balance",
            "created_at",
            "user_id"
        ]
        read_only_fields = ["id",
                            "balance",
                            "created_at",
                            "user_id"]
        extra_kwargs = {
            "economic_consultance": {"required": False}
        }

    def update(self, instance, validated_data):
        if "economic_consultance" in validated_data:
            economicGet = get_object_or_404(
                EconomicConsultant, name=validated_data["economic_consultance"]["name"])
            instance.economic_consultance = economicGet
            instance.save()

        if "insurance" in validated_data:
            accInsurance = []

            for insurance in validated_data["insurance"]:
                insuranceGet = Insurance.objects.filter(
                    name=insurance["name"]).first()
                if not insuranceGet:
                    raise serializers.ValidationError(
                        detail=({"ValueError": f"Not found the insurance with name: {insurance['name']}"}))
                accInsurance.append(insuranceGet)
            instance.insurance.set(accInsurance)
            instance.save()

        return instance
