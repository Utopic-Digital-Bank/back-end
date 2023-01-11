from rest_framework import permissions
from account.models import Account
import ipdb
class OnlyADMlistOpenToPost(permissions.BasePermission):
    
    
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_superuser
        
        return True

class OnlyADMorOwner(permissions.BasePermission):

        def has_object_permission(self, request, view, obj):
            if request.method == "DELETE":
                return request.user.is_superuser
             

            if not request.user.is_superuser:
                account= Account.objects.get(user_id=request.user.id)
                return account.id == obj.account_id
            
            return True