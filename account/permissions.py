from rest_framework import permissions
from users.models import User
from .models import Account
from rest_framework.views import View
import ipdb


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        account_id = request.parser_context["kwargs"]["account_id"]
        account = Account.objects.filter(id=account_id)
        if not account:
            return True
        account = Account.objects.get(id=account_id)

        return (account.user_id == request.user.id)


class IsUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        account_id = request.parser_context["kwargs"]["account_id"]
        account = Account.objects.filter(id=account_id)
        if not account:
            return True
        account = Account.objects.get(id=account_id)

        return (account.user_id == request.user.id) or (request.user.is_superuser)
