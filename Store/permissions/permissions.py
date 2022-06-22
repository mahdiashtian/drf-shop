from rest_framework.permissions import BasePermission , SAFE_METHODS
from rest_framework import authentication

class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is staff as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsAuthor(BasePermission):
    message = 'شما حق انجام این عملیات را ندارید'

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.user or request.user.is_superuser)