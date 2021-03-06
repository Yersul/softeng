from rest_framework.permissions import BasePermission


class PostOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_staff:
            return True

        return False
