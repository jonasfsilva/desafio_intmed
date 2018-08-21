from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    message = "Você não é um administrado."
	
    def has_permission(self,request,view):
        return request.user.is_staff