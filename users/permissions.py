from rest_framework import permissions
from .models import User
import ipdb


class OnlyADMlistOpenToPost(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_superuser

        return True


class OnlyADMorOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(
            id=request.parser_context['kwargs']['user_id'])
        if not user:
            return True
        user = User.objects.get(
            id=request.parser_context['kwargs']['user_id'])

        return request.user.id == user.id or request.user.is_superuser
