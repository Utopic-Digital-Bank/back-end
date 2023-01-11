from extract.serializers import ExtractSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.permissions import IsAccountOwner, IsUserOrAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404
from .models import Extract
from account.models import Account
from drf_spectacular.utils import extend_schema
import ipdb


@extend_schema(tags=["extract"])
class ListExtract (generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOrAdmin]
    serializer_class = ExtractSerializer
    lookup_url_kwarg = "account_id"

    def get_queryset(self):
        return Extract.objects.filter(account_id=self.request.parser_context["kwargs"]["account_id"])


@extend_schema(tags=["account"])
class CreateExtract(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = ExtractSerializer
    queryset = Extract.objects.all()
    lookup_url_kwarg = "account_id"

    def create(self, request, *args, **kwargs):
        SAIDA = ["saque", "pagamento", "pix", "transferência"]

        serializer = ExtractSerializer(Extract, data=request.data)
        serializer.is_valid(raise_exception=True)

        account = get_object_or_404(
            Account, id=self.request.parser_context["kwargs"]["account_id"])
        if (request.data['operation'] in SAIDA and account.balance < request.data['valueOperation']):
            return Response({"valueInsuficient": "The account balance is not enough for the transaction"}, status.HTTP_402_PAYMENT_REQUIRED)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(account_id=self.request.parser_context["kwargs"]["account_id"])
