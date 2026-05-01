from rest_framework.permissions import BasePermission

class IsHost(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=='host'

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        # return request.user.is_authenticated and request.user.role=='admin'
        return(
            request.user.is_authenticated and (
            request.user.role=='admin' or request.user.is_staff or request.user.is_superuser)
        )

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self,request,view,obj):
        # if request.user.is_authenticated and request.user.role='admin':
        if request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.is_staff or request.user.is_superuser
        ):
            return True
        return obj.user==request.user
    
