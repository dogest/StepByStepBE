from rest_framework import serializers

from Account.serializers import UserDetailSerializer
from Plan.models import Plan, PlanUser


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'area', 'name')

class PlanWithContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'area', 'name', 'content')

class PlanUserSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    user = UserDetailSerializer(source='user.userdetail')
    plan = PlanSerializers()

    class Meta:
        model = PlanUser
        fields = ('id', 'plan', 'sort', 'user')
