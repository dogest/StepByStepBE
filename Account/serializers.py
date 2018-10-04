from rest_framework import serializers

from Account.models import User, UserDetail
from Area.serializers import AreaSerializers


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    # 用户的类型由注册方式确定，不应被修改
    user_type = serializers.CharField(read_only=True)
    area = AreaSerializers()

    class Meta:
        model = UserDetail
        fields = ('nickname', 'user_type', 'area')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    userdetail = UserDetailSerializer()
    # 管理员无法修改用户名（但是可以修改昵称）
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'userdetail', 'email')
