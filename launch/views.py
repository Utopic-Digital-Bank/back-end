from rest_framework import generics
from rest_framework.views import Response, status

from .models import Launch
from .serializers import LaunchSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from card.models import Card
from invoices.models import Invoice
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["launch"])
class LaunchView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer

    def get_queryset(self):
        get_object_or_404(Invoice, id=self.kwargs["card_id"])
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        card = get_object_or_404(
            Card, id=self.kwargs["card_id"],
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if card.is_active is False:
            return Response({"msg": "card invalid"}, status.HTTP_403_FORBIDDEN)

        if card.type is "Debit":
            return Response({"msg": "type card invalid"}, status.HTTP_403_FORBIDDEN)

        if card.available_limit < request.data['value']:
            return Response(
                {"msg": "card limit exceeded"}, status.HTTP_402_PAYMENT_REQUIRED
            )

        card.available_limit -= request.data['value']
        card.save()

        value_parcel = round(request.data['value']/request.data['parcel'], 2)
        request.data['value'] = value_parcel

        launch = LaunchSerializer(data=request.data)
        launch.is_valid(raise_exception=True)

        launch = launch.create(launch.validated_data)

        date = launch.date_hour
        day = int(card.due_date) - 5
        month = date.strftime("%m")
        month = int(month)
        year = date.strftime("%Y")

        next_month = int(date.strftime("%d")) >= (int(card.due_date) - 5)

        for index in range(request.data['parcel']):
            if next_month:
                month += (1 + index)
            else:
                month += index

            if month > 12:
                month = 1
                year = int(year) + 1

            invoice = Invoice.objects.filter(
                card_id=self.kwargs["card_id"], closing_date=f'{year}-{month}-{day}')

            if invoice:
                invoice = Invoice.objects.get(
                    card_id=self.kwargs["card_id"], closing_date=f'{year}-{month}-{day}')
                invoice = Invoice.objects.get(id=invoice.id)
                invoice.launch.add(launch)
                invoice.save()
            else:
                invoice.value = value_parcel
                invoice = Invoice.objects.create(
                    closing_date=f'{year}-{month}-{day}', value=value_parcel, due_date=f'{year}-{month}-{card.due_date}', card_id=self.kwargs["card_id"])
                invoice.launch.add(launch)

        return Response(serializer.data, status.HTTP_201_CREATED)
