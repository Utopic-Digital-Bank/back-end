from rest_framework import permissions
from users.models import User
from account.models import Account
from .models import Launch
from rest_framework.views import View
import ipdb


class IsAccountOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        account = Account.objects.get(
            id=request.stream.resolver_match.kwargs["account_id"])

        return account.user.id == request.user.id
