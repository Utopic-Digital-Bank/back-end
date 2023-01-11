from rest_framework import permissions
from users.models import User
from .models import Launch
from account.models import Account
from card.models import Card
from rest_framework.views import View
import ipdb


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        card = Card.objects.get(
            id=request.stream.resolver_match.kwargs["card"])
        account = Account.objects.get(id=card.account_id)

        return account.user.id == request.user.id
