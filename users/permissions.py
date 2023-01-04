from rest_framework import permissions

import ipdb
class OnlyADMlistOpenToPost(permissions.BasePermission):
    
    
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_superuser
        
        return True
        