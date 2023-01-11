from .models import Invoice
from .serializers import InvoiceSerializer
from account.models import Account
from .permissions import IsCardOwner, IsCardOwnerOrAdmin
from card.models import Card
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["invoice"])
class InvoiceView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCardOwnerOrAdmin]

    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.filter(card_id=self.kwargs["card_id"])

    def perform_create(self, serializer):
        card = get_object_or_404(Card, id=self.kwargs['card_id'])
        serializer.is_valid(raise_exception=True)
        serializer.save(card=card)


@extend_schema(tags=["invoice"])
class InvoiceDetailView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCardOwner]

    def perform_update(self, serializer):
        card = get_object_or_404(Card, id=self.kwargs['card_id'])
        account = get_object_or_404(Account, id=self.kwargs['account_id'])
        if account.balance >= self.value:
            account.balance -= self.value
            self.paid = True
            account.save()
            return self.save()
