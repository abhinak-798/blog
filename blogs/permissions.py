from rest_framework.permissions import BasePermission


class IsAutherOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method=="GET":
            return True
        return request.user.is_authenticated

    def has_object_permission(self,request,view,obj):
        return obj.author==request.user