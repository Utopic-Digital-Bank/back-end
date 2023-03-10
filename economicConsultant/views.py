from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import EconomicConsultant
from .serializers import EconomicConsultantSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["economic consultant"])
class EconomicConsultantView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = EconomicConsultantSerializer
    queryset = EconomicConsultant.objects.all()
