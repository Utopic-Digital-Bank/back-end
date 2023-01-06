from rest_framework import permissions

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
                return request.user.id == obj.id
            
            return True