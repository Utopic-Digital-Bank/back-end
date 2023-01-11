from .models import Account
from .serializers import AccountSerializer, UpdateAccount
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner, IsUserOrAdmin
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.views import Response, status
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["account"])
class AccountView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOrAdmin]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        account = Account.objects.filter(user_id=request.user.id)
        if account:
            return Response(
                {"hasAccount": "It is not allowed to have more than one account."}, status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):

        serializer.save(user_id=self.request.user.id)


@extend_schema(tags=["account"])
@extend_schema(methods=["PUT"], exclude=True)
class AccountDetails(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = UpdateAccount
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        account = Account.objects.filter(id=self.kwargs['pk'])
        return account
