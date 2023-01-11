from rest_framework import serializers
from .models import Account
from django.shortcuts import get_object_or_404
import ipdb
from insurance.models import Insurance
from economicConsultant.models import EconomicConsultant

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "balance",
            "created_at",
            "user_id"
        ]
        read_only_fields = [ "id",
            "balance",
            "created_at",
            "user_id"]



class UpdateAccount(serializers.ModelSerializer):
    insurance = serializers.ListField()
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
        read_only_fields = [ "id",
            "balance",
            "created_at",
            "user_id"]
        extra_kwargs = {
            "insurance": {"required":False},
            "economic_consultance": {"required": False}
            }


    def update(self, instance: Account, validated_data):
        accInsurance = []

        if "insurance" in validated_data:
            insuranceList = validated_data["insurance"]
            for insurance in insuranceList:
                insuranceGet = Insurance.objects.filter(name = insurance)
                if not insuranceGet:
                    raise ValueError(f"Not found the insurance {insurance}")
            insuranceGet = Insurance.objects.get(name = insurance)
            accInsurance.append(insuranceGet.id)

            instance.insurance.set(accInsurance)
        


        if "economic_consultance" in validated_data:
            ipdb.set_trace()
            consultance = validated_data["economic_consultance"]
            consultanceGet = get_object_or_404(EconomicConsultant, id = consultance.id)
            if not consultanceGet:
                raise ValueError(f"Not found the consultance {consultance}")
            aq = instance.economic_consultance.set(consultanceGet.id)
        return instance

        
    




            
            
        
        