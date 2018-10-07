from rest_framework import serializers

from Area.models import Area


class AreaSerializers(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True)

    class Meta:
        model = Area
        fields = ('short_name', 'name', 'code', 'content')


class AreaByOwnerOrRootSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('short_name', 'name', 'code', 'content')
