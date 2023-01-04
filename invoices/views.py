from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class InvoiceView(generics.ListCreateAPIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def perform_create(self, serializer):
        serializer.save(invoice=self.request.invoice)