from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    
    def has_permission(self,request,view):
        
        if request.user.is_authenticated and request.user.username =='owner' :
            return True
        else :
            return False 
    


