from rest_framework.permissions import BasePermission,SAFE_METHODS
'''
class IsOwner(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user==request.user
'''

class IsHost(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=='host'
class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=="admin"
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user.is_authenticated and request.user.role=="admin":
            return True
        return obj.user==request.user



from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsHost(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=='host'

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=='admin'

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user.is_authenticated and request.user.role=='admin':
            return True
        return obj.user==request.user
    

