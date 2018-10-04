from rest_framework import serializers

from Area.models import Area


class AreaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('url', 'short_name', 'name')
