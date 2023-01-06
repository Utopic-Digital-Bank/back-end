from rest_framework import serializers
from .models import Extract
from account.models import Account

class ExtractSerializer(serializers.ModelSerializer):
    class Meta:
        current_balance = serializers.SerializerMethodField()
        model = Extract
        fields = [
        "valueOperation",
        "previous_balance",
        "current_balance",
        "operation", 
        "creation_date",
        "account_id",
        ]
        extra_kwargs = {"previous_balance": {"read_only": True}, "current_balance": {"read_only": True}}
        
        def get_current_balance(self, obj):
            account = Account.object.get(self.account_id==id)
            return account.balance

        def get_current_balance(self, obj):
            account = Account.object.get(self.account_id==id)
            return (account.balance - self.valueOperation)

