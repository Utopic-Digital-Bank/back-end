from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import UserSerializer, CustomJWTSerializer

from .models import User
from .permissions import OnlyADMlistOpenToPost
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


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


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [OnlyADMlistOpenToPost]

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
