from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from users.serializers import UserSerializer, CustomJWTSerializer
from .models import User
from .permissions import OnlyADMlistOpenToPost, OnlyADMorOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
import ipdb


@extend_schema(tags=["login"])
class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

    def post(self, request, *args, **kwargs):
        if ("cpf" not in request.data.keys()):
            return Response({"cpf": ["This field is required"]}, status.HTTP_400_BAD_REQUEST)

        username = ""
        cpf = request.data["cpf"]

        for number in cpf:
            if number == " " or number == "." or number == "-":
                continue
            username = username + number
        request.data["username"] = username
        request.data.pop('cpf')

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


@extend_schema(tags=["user"])
class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [OnlyADMlistOpenToPost]
    serializer_class = UserSerializer

    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)

        user.save()
        return Response(user.data, status.HTTP_201_CREATED)

    def get(self, request):
        user = User.objects.all()
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


@extend_schema(tags=["user"])
class UserDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [OnlyADMorOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"

    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
