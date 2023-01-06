from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if not request.user.is_superuser:
            return obj == request.user
        return True
        
        # return request.user.is_authenticated and obj == request.user