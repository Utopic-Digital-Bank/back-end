from .models import Account
from .serializers import AccountSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics


class AccountView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)