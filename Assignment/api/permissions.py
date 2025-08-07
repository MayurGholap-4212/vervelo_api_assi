from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsStaffOrSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.is_super_admin
    