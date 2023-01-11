from rest_framework.views import APIView, Response, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from card.models import Card
from account.models import Account
from users.models import User
from .serializers import CardSerializer
from .permissions import OnlyADMorOwner
from django.shortcuts import get_object_or_404
import random
import datetime
import cryptocode
import ipdb
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["card"])
class CardView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer

    def post(self, request):
        #PESQUISA A ACCOUNT REFERENTE AO CARTÃO
        account = get_object_or_404(Account, user_id = request.user.id)

        #VERIFICA SE O USUÁRIO TEM UM CARTÃO DO TIPO PASSADO
        card_already_exists = Card.objects.filter(account_id= account.id, type = request.data["type"]).exists()
        if card_already_exists:
            r=request.data["type"]
            raise ValueError(f"Usuário já tem um cartão do tipo {r}")

        # GERA O NÚMERO DO CARTÃO
        number = random.randint(1000000000000000, 9999999999999999)

        #VERIFICA O TAMANHO DA SENHA
        if len(request.data["password"]) != 4:
            raise ValueError("Password deve ter 4 dígitos")


        try:
            numberAlreadyExists = Card.objects.get(number=number)
            if numberAlreadyExists:
                number = random.randint(1000000000000000, 9999999999999999)
        except:
            pass

        # CRIANDO O HASH DO CARTÃO
        number_to_string = str(number)
        key = "cardcrypto"
        card_encoded = cryptocode.encrypt(number_to_string, key)

        # GERA O CVV
        cvv = random.randint(100, 999)
        try:
            cvv_already_exists = Card.objects.get(cvv=cvv)
            if cvv_already_exists:
                cvv = random(100, 999)
        except:
            pass

        
        #CRIA O HASH DO CVV
        cvv_to_string = str(cvv)
        cvv_encoded = cryptocode.encrypt(cvv_to_string, key)


        #GERA A DATA DE EXPIRAÇÃO DO CARTÃO

        date_now = datetime.datetime.now()
        year = date_now.year
        due_card = f"{date_now.month}-{year+4}"

        # DEFINE O LIMITE DO CARTÃO
        if request.data["type"] == "Credit" or request.data["type"] == "Múltiplo":

            income = User.objects.get(id=request.user.id)
            total_limit = income.monthly_income * 0.7
        else:
            total_limit = 0.0

        # CRIA O HASH DE SENHA

        key = "cardcrypto"
        password_encoded = cryptocode.encrypt(
            str(str(request.data["password"])), key)



        card = CardSerializer(data=request.data)
        card.is_valid(raise_exception=True)

        card.save(number=card_encoded, cvv=str(cvv), balance_invoices=0, due_card=due_card,
                  total_limit=total_limit, available_limit=total_limit, account_id=account.id,
                  password=password_encoded
                  )


        card_decoded = cryptocode.decrypt(card_encoded, key)

        number_card = {"number": card_decoded}
        dict_return = {}
        dict_return.update(number_card)
        for _ in card.data:
            dict_return.update(card.data)


        dict_return["password"] = request.data["password"]
        dict_return["cvv"]=cvv


        return Response(dict_return, status.HTTP_201_CREATED)


@extend_schema(tags=["card"])
@extend_schema(methods=["PUT"], exclude=True)
class CardDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, OnlyADMorOwner]
    serializer_class = CardSerializer

    def patch(self, request, card_id):
        card = get_object_or_404(Card, id=card_id)
        self.check_object_permissions(request, card)
        serializer = CardSerializer(card, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, card_id):
        card = get_object_or_404(Card, id=card_id)
        self.check_object_permissions(request, card)
        card.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
