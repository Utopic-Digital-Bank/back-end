from .models import Invoice
from .serializers import InvoiceSerializer
from account.models import Account
from card.models import Card
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

""" class InvoiceView(generics.ListCreateAPIView):

    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    def perform_create(self, serializer):
        card = get_object_or_404(Card, id=self.kwargs['card_id'])

        account = get_object_or_404(Account, id=self.kwargs['account_id'])
        serializer.save(card_id=self.kwargs["card_id"]) """

class InvoiceDetailView(generics.UpdateAPIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_update(self, serializer):
        card = get_object_or_404(Card, id=self.kwargs['card_id'])
        account = get_object_or_404(Account, id=self.kwargs['account_id'])
        if account.balance >= self.value:
            account.balance -= self.value
            self.paid = True
            account.save()
            return self.save()