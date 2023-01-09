from account.serializers import AccountSerializer
from extract.serializers import ExtractSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from account.permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404
from economicConsultant.models import EconomicConsultant
from insurance.models import Insurance
from .models import Extract
from account.models import Account


class ListExtract (generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = Extract
    queryset = Extract.objects.all()


class CreateExtract(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = Extract
    queryset = Extract.objects.all()
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
     #   Atualiza somente o balance
        account = get_object_or_404(Account, id=self.kwargs["pk"])
        valueOperation = self.valueOperation
        self.previous_balance = account.balance

        if self.operation == "DEPOSITO":
            self.current_balance = self.valueOperation + self.previous_balance
            account.balance = (self.previous_balance + valueOperation)
            account.save()
        else:
            self.current_balance = self.valueOperation - self.previous_balance
            self.previous_balance = self.current_balance
            account.balance = (self.previous_balance - valueOperation)
            account.save()
        serializer.save(self)
