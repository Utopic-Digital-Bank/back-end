from rest_framework import permissions
from users.models import User
from account.models import Account
from card.models import Card
from rest_framework.views import View
import ipdb


class IsCardOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        card_id = request.parser_context['kwargs']['card_id']
        card = Card.objects.get(id=card_id)
        account = Account.objects.get(id=card.account_id)
        return (account.user_id == request.user.id) or (
            request.user.is_superuser)


class IsCardOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        card_id = request.parser_context['kwargs']['card_id']
        card = Card.objects.get(id=card_id)
        account = Account.objects.get(id=card.account_id)

        return account.user_id == request.user.id
