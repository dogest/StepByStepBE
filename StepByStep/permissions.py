from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsRootOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            (
                request.user and request.user.is_authenticated and
                (
                    request.user.is_staff or
                    (
                        request.user.userdetail and
                        request.user.userdetail.user_type == 'root'
                    )
                )
            )
        )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


def IsRoot(user):
    """
    判断用户是否拥有 root 权限
    """
    if not user or not user.is_authenticated:
        return False
    if user.is_staff:
        return True
    if user.userdetail and user.userdetail.user_type == 'root':
        return True
    return False


def IsAreaAdmin(area, user):
    """
    判断用户是否是指定域的管理员
    """
    if not user or not user.is_authenticated:
        return False
    if user.userdetail and user.userdetail.user_type == 'admin' and user.userdetail.area == area:
        return True
    return False
