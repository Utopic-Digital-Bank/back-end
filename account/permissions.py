from rest_framework import permissions
from users.models import User
from .models import Account
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj:Account) -> bool:
        if request.method == "PATCH":
            return request.user.is_superuser
        if request.user.is_superuser:
            return True
        return obj.user_id == request.user.id

