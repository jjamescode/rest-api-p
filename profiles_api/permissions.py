from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit their profile"""

    def has_object_permission(self, request, view, obj):
        "Checks if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        "Checks if user is trying to edit their own statis"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
