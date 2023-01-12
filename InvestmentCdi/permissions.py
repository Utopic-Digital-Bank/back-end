from rest_framework import permissions
from users.models import User
from account.models import Account
from rest_framework.views import View
import ipdb


class IsAccountOwner(permissions.BasePermission):

    def has_permission(self, request, view) -> bool:
        account_id = request.parser_context["kwargs"]["account_id"]
        account = Account.objects.filter(id=account_id)
        if not account:
            return True
        account = Account.objects.get(id=account_id)
        if request.method == "GET":
            if request.user.is_superuser:
                return True

        return (account.user_id == request.user.id)

    def has_object_permission(self, request, view, obj):
        account_id = request.parser_context["kwargs"]["account_id"]
        account = Account.objects.filter(id=account_id)
        if not account:
            return True
        account = Account.objects.get(id=account_id)
        if request.method == "GET":
            if request.user.is_superuser:
                return True
        return account.id == obj.account_id
