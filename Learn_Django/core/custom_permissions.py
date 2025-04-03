from rest_framework import permissions
from django.contrib.auth.models import User

class IsStaffEditorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        # Must have at least view permission 
        if user.is_staff and user.has_perm('teacher.view_teacherprofile'):  #app_name.verb_model_name
            print('Access granted!')
            return True
        print('Access denied!')
        return False
    

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]