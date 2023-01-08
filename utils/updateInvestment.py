from django.shortcuts import *
from datetime import date
import requests
import json

from InvestmentCdi.models import InvestmentCdi


def UpdateInvestment(investment: InvestmentCdi) -> InvestmentCdi:
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
