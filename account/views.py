from .models import Account
from .serializers import AccountSerializer, UpdateAccount
from extract.serializers import ExtractSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from django.shortcuts import get_object_or_404
from economicConsultant.models import EconomicConsultant
from insurance.models import Insurance
from extract.models import Extract
# from drf_spectacular.utils import extend_schema

import ipdb

class AccountView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = PageNumberPagination
    def perform_create(self, serializer): 
        serializer.save(user_id=self.request.user.id)


# @extend_schema(methods=["PUT"], exclude=True)
class AccountDetails(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = UpdateAccount
    queryset = Account.objects.all()
    lookup_url_kwarg = "pk"
    


    #def perform_update(self, serializer):
        
    #     insuranceList = self.request.data["insurance"]
    #     consultance = self.request.data["economic_consultance"]
        
    #     if insuranceList:
    #         for insurance in insuranceList:
    #             insuranceGet = get_object_or_404(Insurance, name = insurance)

    #         ...
            
    #     if consultance:
            
    #         ...
        
    #     serializer.save(user_id=self.request.user.id)

#  accInsurance = []
#         for insurance in insuranceList:
#             insuranceGet = get_object_or_404(Insurance, name = insurance)
#             accInsurance.append(insuranceGet)
#         if len(insuranceList)>0:
#             accountOwner = Account.objects.get(user_id= self.request.user.id)
#             accountOwner.insurance.clear()
#             accountOwner.insurance.set(accInsurance)



#         EconomicGet = get_object_or_404(EconomicConsultant, id = self.request.data["economic_consultance"])
#         #ipdb.set_trace()
#         accountOwner.economic_consultance.set(EconomicGet)
#         accountOwner.save()