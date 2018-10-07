from rest_framework import serializers

from Account.models import User, UserDetail
from Area.serializers import AreaSerializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    id = serializers.IntegerField(source='user.id')
    # 管理员无法修改用户名（但是可以修改昵称）
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email')
    # 用户的类型由注册方式确定，不应被修改
    user_type = serializers.CharField(read_only=True)
    area = AreaSerializers()

    class Meta:
        model = UserDetail
        fields = ('id', 'username', 'email', 'nickname', 'user_type', 'area', 'user',
                  'school', 'college', 'major', 'team')
