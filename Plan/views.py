from rest_framework import viewsets
from rest_framework.response import Response

from Plan.models import Plan, PlanProblem, PlanUser
from Plan.permissions import PlanPermission
from Plan.serializers import PlanSerializers
from StepByStep.permissions import IsAdmin


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    permission_classes = (PlanPermission,)
    filter_fields = ('area',)

    def create(self, request):
        """
        创建计划，仅域管理员可用，会自动创建到管理员所在域
        """
        if not IsAdmin(request.user):
            return Response({
                'user_type': ['只有域管理员可以创建 Plan']
            }, 403)
        area = request.user.userdetail.area
        name = request.data.get('name')
        if name is None:
            return Response({
                'name': ['这个参数是必须的']
            }, 400)
        plan = Plan()
        plan.area = area
        plan.name = name
        plan.save()
        return Response({
            'id': plan.id,
            'area': area.id,
            'name': name
        }, 201)
