from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Account.serializers import UserSerializer


class SessionApiView(APIView):
    # 仅登陆用户可用
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_authenticated:
            user_deatil = request.user.userdetail
            return Response({
                'id': request.user.id,
                'username': request.user.username,
                'nickname': user_deatil.nickname,
                'type': user_deatil.user_type,
            })
        return Response({
            'logined': False
        })


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    # 仅返回体系内的用户，django 自带的管理员不应纳入此体系中（他的地位比体系内所有用户都高）
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
