from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from card.models import Card
from account.models import Account

from .serializers import CardSerializer

from users.permissions import OnlyADMorOwner
from django.shortcuts import get_object_or_404

import random
import datetime

class CardView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self, request):
        #GERA O NÚMERO DO CARTÃO
        number = random.randint(1000000000000000,9999999999999999)
        try:
            numberAlreadyExists= Card.objects.get(number=number)
            if numberAlreadyExists:
                number = random.randint(1000000000000000,9999999999999999)
        except:
            pass

        #GERA O CVV
        cvv = random.randint(100,999)
        try:
            cvv_already_exists= Card.objects.get(cvv=cvv)
            if cvv_already_exists:
                cvv = random(100,999)
        except:
            pass
        
        #GERA A DATA DE EXPIRAÇÃO DO CARTÃO
        date_now = datetime.datetime.now()
        year= date_now.year
        due_card= f"{date_now.month}/{year+4}"

        #DEFINE O LIMITE DO CARTÃO
        if request.data["type"] == "Credit" or request.data["type"]=="Múltiplo":
            balance =  Account.objects.get(user_id= request.user.id)
            total_limit= balance["balance"] * 3
        else:
            total_limit= 0.0

        card = CardSerializer(data= request.data)
        card.is_valid(raise_exception=True)
        card.save(number=str(number),cvv= str(cvv), invoice_balance=0, due_card= due_card, total_limit= total_limit, available_limit= total_limit)

        return Response(card.data, status.HTTP_201_CREATED)


class CardDetailView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated, OnlyADMorOwner]
    def patch(self, request, card_id):
        card = get_object_or_404(Card, id=card_id)
        self.check_object_permissions(request, card)
        serializer = CardSerializer(card,request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def delete(self, request, card_id):
        card = get_object_or_404(Card, id=card_id)
        self.check_object_permissions(request, card)
        card.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


