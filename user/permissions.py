from rest_framework.permissions import (SAFE_METHODS, BasePermission)

class UserPermissions(BasePermission):
    '''
    Default User object permissions
    '''

    def has_object_permission(self, request, view, obj):
        # ! make sure READ-ONLY access is given
        if request.method in SAFE_METHODS:
            return True
        # ! write permissions for owner of object
        return obj == request.user
