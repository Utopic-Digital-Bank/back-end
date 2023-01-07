from .models import Account
from .serializers import AccountSerializer, UpdateAccount
from extract.serializers import ExtractSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404
from economicConsultant.models import EconomicConsultant
from insurance.models import Insurance
from extract.models import Extract
# from drf_spectacular.utils import extend_schema



class AccountView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        insuranceGet = get_object_or_404(Insurance, id = self.kwargs["pk"])
        economicGet = get_object_or_404(EconomicConsultant, id = self.kwargs["pk"])
        serializer.save(user_id=self.request.user, insurance_id= insuranceGet, economic_consultant_id= economicGet)

# @extend_schema(methods=["PUT"], exclude=True)
class AccountDetails(generics.RetrieveUpdateAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated, IsAccountOwner]
        serializer_class = UpdateAccount
        queryset = Account.objects.all()
        lookup_url_kwarg = "pk"

