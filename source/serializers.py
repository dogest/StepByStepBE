from rest_framework import serializers

from source.models import Source, UserBindSource


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('name', 'url', 'created_at')


class UserBindSourceSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.StringRelatedField(source='user.username')

    class Meta:
        model = UserBindSource
        fields = ('username', 'source', 'username', 'created_at')
