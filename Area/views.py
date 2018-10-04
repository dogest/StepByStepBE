from rest_framework import viewsets

from Area.models import Area
from Area.serializers import AreaSerializers
from StepByStep.permissions import IsRootOrReadOnly


class AreaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsRootOrReadOnly,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
