from rest_framework import permissions
from users.models import User
from account.models import Account
from rest_framework.views import View
import ipdb


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        account = Account.objects.get(id=obj.account_id)
        if (request.method == "POST" or request.method == "DELETE"):
            if (account.user == request.user):
                return True
            else:
                return False
        if (account.user == request.user):
            return True
        if request.user.is_superuser:
            return True
        return False
