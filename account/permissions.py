from rest_framework import permissions
from users.models import User
from .models import Account
from rest_framework.views import View
import ipdb


class IsAccountOwner(permissions.BasePermission):

    def has_permission(self, request, view) -> bool:
        account = Account.objects.filter(
            user_id=request.parser_context["kwargs"]["pk"])
        if not account:
            return True

        return (account.user_id == request.user.id) or (request.user.is_superuser)


class IsUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == "GET":
            return request.user.is_superuser

        return super().has_permission(request, view)
