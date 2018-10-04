from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from Area.models import Area
from Area.serializers import AreaSerializers


class AreaViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
