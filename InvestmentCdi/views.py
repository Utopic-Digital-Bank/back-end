from django.shortcuts import *
from rest_framework.views import Response, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import date
import json
import requests
import ipdb

from .serializers import InvestmentCdiSerializer, GetAllInvestmentCdiSerializer
from InvestmentCdi.models import InvestmentCdi
from account.models import Account


class InvestmentCdiView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []
    serializer_class = GetAllInvestmentCdiSerializer
    queryset = InvestmentCdi.objects.all()


class InvestmentCdiDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []
    serializer_class = InvestmentCdiSerializer

    def get_queryset(self):
        investment = get_object_or_404(InvestmentCdi, id=self.kwargs["pk"])

        data_inicio = investment.creation_date
        data_fim = date.today().strftime("%Y-%m-%d")
        value = investment.initial_value
        value = float(value)

        url = f"https://calculadorarendafixa.com.br/calculadora/di/calculo?dataInicio={data_inicio}&dataFim={data_fim}&percentual=100.00&valor={value}"
        response_b3 = requests.get(url)
        response_b3 = json.loads(response_b3.content)

        investment.current_value = float(response_b3['valorCalculado'])
        investment.yield_value = (
            float(response_b3['valorCalculado']) - float(response_b3['valorBase']))

        investment.save()
        return InvestmentCdi.objects.all()

    def perform_destroy(self, instance):
        investment = get_object_or_404(InvestmentCdi, id=self.kwargs["pk"])

        data_inicio = investment.creation_date
        data_fim = date.today().strftime("%Y-%m-%d")
        value = investment.initial_value
        value = float(value)

        url = f"https://calculadorarendafixa.com.br/calculadora/di/calculo?dataInicio={data_inicio}&dataFim={data_fim}&percentual=100.00&valor={value}"
        response_b3 = requests.get(url)
        response_b3 = json.loads(response_b3.content)

        investment.current_value = float(response_b3['valorCalculado'])
        investment.yield_value = (
            float(response_b3['valorCalculado']) - float(response_b3['valorBase']))

        investment.save()

        account = Account.objects.get(id=investment.account_id)

        account.balance = float(account.balance) + \
            float(investment.current_value)
        account.save()

        return investment.delete()
