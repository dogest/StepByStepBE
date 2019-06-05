from rest_framework import serializers

from account.models import UserDetail


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('username', 'github_id', 'node_id', 'avatar_url', 'gravatar_id',
                  'url', 'html_url', 'name', 'blog', 'location', 'email', 'bio')
