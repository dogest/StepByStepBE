from rest_framework import viewsets

from source.models import Source, UserBindSource
from source.serializers import SourceSerializer, UserBindSourceSerializer
from StepByStepBE.permissions import IsAdminOrReadOnly


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = (IsAdminOrReadOnly,)


class UserBindSourceViewSet(viewsets.ModelViewSet):
    queryset = UserBindSource.objects.all()
    serializer_class = UserBindSourceSerializer
    permission_classes = (IsAdminOrReadOnly,)
