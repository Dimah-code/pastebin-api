from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owner of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        """
        Allow safe methods(read) for all users
        and edit or delete methods allow just for owner
        """
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.owner
