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
    insurance_id = serializers.ListField()
    class Meta:
        model = Account
        fields = [
        "insurance_id",
        "economic_consultance_id",
        "id",
        "balance",
        "created_at",
        "user_id"
        ]
        read_only_fields = [ "id",
            "balance",
            "created_at",
            "user_id"]


    def update(self, instance, validated_data):
        insuranceList = [self.request.data.insurance]
        accInsurance = []
        for insurance in insuranceList:
            insuranceGet = get_object_or_404(Insurance, name = insurance.name)
            accInsurance.append(insuranceGet)
        ipdb.set_trace()
        if insuranceList.len > 0:
            accountOwner = Account.objects.filter(user_id= self.request.user.id)
            accountOwner.insurance.clear()
            self.add(insurance_id = accInsurance)
        
        EconomicGet = get_object_or_404(EconomicConsultant, name = self.request.name)
        self.save(user_id=self.request.user.id, economic_consultant_id = EconomicGet.id)
        return super().update(instance, validated_data)