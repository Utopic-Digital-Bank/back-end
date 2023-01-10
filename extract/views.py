from extract.serializers import ExtractSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404
from .models import Extract
from account.models import Account
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["extract"])
class ListExtract (generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = ExtractSerializer
    queryset = Extract.objects.all()


@extend_schema(tags=["account"])
class CreateExtract(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = ExtractSerializer
    queryset = Extract.objects.all()
    lookup_url_kwarg = "account_id"

    def create(self, request, *args, **kwargs):
        SAIDA = ["saque", "pagamento", "pix", "transferência"]

        account = Account.objects.get(id=self.kwargs["account_id"])
        if (request.data['operation'] in SAIDA and account.balance < request.data['valueOperation']):
            return Response({"valueInsuficient": "The account balance is not enough for the transaction"}, status.HTTP_402_PAYMENT_REQUIRED)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(account_id=self.kwargs["account_id"])
