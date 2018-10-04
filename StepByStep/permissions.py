from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsRootOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            (
                request.user and (
                    request.user.is_staff or
                    request.user.userdetail.user_type == 'root'
                )
            )
        )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
