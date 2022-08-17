from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj=None):
        """Check user is trying to edit their own profile"""
        print(permissions.SAFE_METHODS)
        print(request.method)
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and not request.user.is_anonymous:
            return obj.id == request.user.id

        return False
