from django.shortcuts import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import status, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import InvestmentCdiSerializer, GetAllInvestmentCdiSerializer
from InvestmentCdi.models import InvestmentCdi
from account.models import Account
from utils.updateInvestment import UpdateInvestment
from .permissions import IsAccountOwner
import ipdb
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["investment cdi"])
class ListCreateInvestmentCdiView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetAllInvestmentCdiSerializer

        elif self.request.method == "POST":
            return InvestmentCdiSerializer

    def get_queryset(self):
        investments = get_list_or_404(
            InvestmentCdi, account_id=self.kwargs["account_id"])

        for investment in investments:
            UpdateInvestment(investment)

        return investments

    def create(self, request, *args, **kwargs):
        account = Account.objects.get(id=self.kwargs["account_id"])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if (account.balance >= request.data["initial_value"]):
            account.balance -= request.data["initial_value"]
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            account.save()
            return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"balanceInsuficient": "account does not have enough balance for the requested investment"}, status.HTTP_402_PAYMENT_REQUIRED)

    def perform_create(self, serializer):
        return serializer.save(account_id=self.kwargs["account_id"])


@extend_schema(tags=["investment cdi"])
@extend_schema(methods=["PUT", "PATCH"], exclude=True)
class InvestmentCdiDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = InvestmentCdiSerializer

    def get_queryset(self):
        investment = get_object_or_404(InvestmentCdi, id=self.kwargs["pk"])
        UpdateInvestment(investment)

        return InvestmentCdi.objects.all()

    def perform_destroy(self, instance):
        investment = get_object_or_404(InvestmentCdi, id=self.kwargs["pk"])

        UpdateInvestment(investment)

        account = Account.objects.get(id=investment.account_id)

        account.balance = float(account.balance) + \
            float(investment.current_value)
        account.save()

        return investment.delete()
