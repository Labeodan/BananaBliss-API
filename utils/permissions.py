from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to allow admin users full CRUD access to orders
    while restricting non-admin users to only their own orders.
    """
    def has_permission(self, request, view):
        # Admins get full access
        if request.user.role == 'admin':
            return True
        # Non-admin users can only view or edit their own orders
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admins can perform any action on any order
        if request.user.role == 'admin':
            return True
        # Non-admin users can only perform actions on their own orders
        return obj.user == request.user
