from rest_framework import serializers

from Area.models import Area


class AreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('short_name', 'name')
