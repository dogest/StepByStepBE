from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from Area.models import Area
from Area.permissions import AreaPermission
from Area.serializers import AreaByOwnerOrRootSerializers, AreaSerializers
from StepByStep.permissions import IsAreaAdmin, IsRoot


class AreaViewSet(viewsets.ModelViewSet):
    permission_classes = (AreaPermission,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
    filter_fields = {
        'name': ('icontains',),
        'short_name': ('icontains',),
    }

    def retrieve(self, request, pk=None):
        queryset = Area.objects.all()
        area = get_object_or_404(queryset, pk=pk)
        # 对于 root 用户或域管理员，同时返回 code
        if IsRoot(request.user) or IsAreaAdmin(area, request.user):
            serializer = AreaByOwnerOrRootSerializers(area)
        else:
            serializer = AreaSerializers(area)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Area.objects.all()
        area = get_object_or_404(queryset, pk=pk)
        if not (IsRoot(request.user) or IsAreaAdmin(area, request.user)):
            return Response({
                'user_type': ['您没有创建用户的权限']
            }, 403)
        area.short_name = request.data.get('short_name')
        area.name = request.data.get('name')
        area.code = request.data.get('code')
        area.content = request.data.get('content')
        area.save()
        return self.retrieve(request, pk)
