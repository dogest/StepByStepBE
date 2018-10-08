from rest_framework.permissions import SAFE_METHODS, BasePermission

from StepByStep.permissions import IsAreaAdmin, IsRoot, IsAdmin


class PlanPermission(BasePermission):
    def has_permission(self, request, view):
        # 对于读取的请求一律放行
        if request.method in SAFE_METHODS:
            return True

        # 更新请求放行到 has_object_permission 函数去处理
        if request.method == 'PUT':
            return True
        # root 用户或域管理员可以新增或删除
        if request.method == 'POST' or request.method == 'DELETE':
            return IsRoot(request.user) or IsAdmin(request.user)
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # root 用户或对应的域管理员可以修改
        if request.method == 'PUT':
            if IsRoot(request.user):
                return True
            if (IsAreaAdmin(obj.area, request.user) and
                    request.data.get('area') == str(obj.area.id)):
                return True
        return False
