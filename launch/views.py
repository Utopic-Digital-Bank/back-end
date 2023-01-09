from rest_framework import generics
from rest_framework.views import Response, status

from .models import Launch
from .serializers import LaunchSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from card.models import Card
from invoices.models import Invoice
from django.shortcuts import get_object_or_404
import datetime


class LaunchView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer

    def create(self, request, *args, **kwargs):
        card = get_object_or_404(
            Card, id=self.kwargs["card_id"], account_id=self.kwargs["account_id"]
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if card.is_active is False:
            return Response({"msg": "card invalid"}, status.HTTP_403_FORBIDDEN)

        if card.type is "Debit":
            return Response({"msg": "type card invalid"}, status.HTTP_403_FORBIDDEN)

        if card.available_limit < request.data.value:
            return Response(
                {"msg": "card limit exceeded"}, status.HTTP_402_PAYMENT_REQUIRED
            )

        card.available_limit -= request.data.value
        card.save()

        value_parcel = round(request.data.value/request.data.parcel, 2)
        request.data.value = value_parcel
        launch = Launch.save(request.data)

        date = datetime.date(request.data.date_hour)
        day = int(card.due_date) - 5
        month = date.strftime("%m")
        year = date.strftime("%Y")
        
        next_month = date.strftime("%d") >= (int(card.due_date) - 5)

        for parcel, index in request.data.parcel:
            if next_month:
                month += (1 + index)
            else:
                month += index
            
            if month > 12:
                month = 1
                year += 1

            invoice = Invoice.objects.get(card_id=self.kwargs["card_id"], closing_date=f'{year}-{month}-{day}')

            if invoice:
                invoice.launch.add(launch)
            else:
                invoice = Invoice.objects.create(closing_date=f'{year}-{month}-{day}')
                invoice.launch.add(launch)


        return Response(serializer.data, status.HTTP_201_CREATED)
