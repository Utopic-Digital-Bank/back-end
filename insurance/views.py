from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from .serializers import InsuranceSerializer
from .models import Insurance
import ipdb
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["insurance"])
class InsuranceViews(ListCreateAPIView):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


@extend_schema(tags=["insurance"])
@extend_schema(methods=["PUT"], exclude=True)
class InsuranceDetailsViews(RetrieveUpdateDestroyAPIView):
    serializer_class = InsuranceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Insurance.objects.filter(id=int(self.kwargs["id"]))

    def update(self, request, *args, **kwargs):
        if ("tuition" in request.data and len(request.data) == 1):
            return super().update(request, *args, **kwargs)

        else:
            return Response({"badRequest": "Only the parameter tuition is alterabled"},
                            status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
