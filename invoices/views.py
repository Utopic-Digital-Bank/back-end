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
import ipdb


@extend_schema(tags=["invoice"])
class InvoiceView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCardOwnerOrAdmin]

    serializer_class = InvoiceSerializer

    def get_queryset(self):
        get_object_or_404(Card, id=self.kwargs['card_id'])
        return Invoice.objects.filter(card_id=self.kwargs["card_id"])

    def perform_create(self, serializer):
        card = get_object_or_404(Card, id=self.kwargs['card_id'])
        serializer.is_valid(raise_exception=True)
        serializer.save(card=card)


@extend_schema(tags=["invoice"])
@extend_schema(methods=["PUT"], exclude=True)
class InvoiceDetailView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCardOwner]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
