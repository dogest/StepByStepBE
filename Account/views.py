from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Account.models import User, UserDetail
from Account.serializers import UserDetailSerializer
from Area.models import Area


class SessionApiView(APIView):
    # 仅登陆用户可用
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_detail = request.user.userdetail
        area = request.user.userdetail.area
        return_data = {
            'id': request.user.id,
            'username': request.user.username,
            'nickname': user_detail.nickname,
            'type': user_detail.user_type,
        }
        if area:
            return_data['area'] = {
                'id': area.id,
                'short_name': area.short_name,
                'name': area.name
            }
        return Response(return_data)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = UserDetail.objects.filter()
    serializer_class = UserDetailSerializer
    filter_fields = {
        'area': ('exact',),
        'nickname': ('icontains',),
        'school': ('icontains',),
        'college': ('icontains',),
        'major': ('icontains',),
        'team': ('icontains',),
    }

    def create(self, request):
        """
        创建用户分为以下几种情况：
        1. django 的管理员创建
            这种情况无需考虑，前台不需要为此创建页面，django 管理员可以由后台进入修改
        2. root 用户（总管理员）
            考虑到业务逻辑，root 用户创建的必定为域管理员（admin）
        3. admin 用户（域管理员）
            无法创建用户（可以修改所在域的用户）
        4. 未登录 or 普通用户
            创建普通用户，需要提供域和邀请码，可以提供学校、学院、系和班级等额外信息
        """
        if request.user.is_staff:
            return Response({
                'user_type': ['您还是去后台添加用户吧']
            }, 403)
        if request.user.is_authenticated:
            if request.user.userdetail.user_type == 'root':
                username = request.data.get('username')
                nickname = request.data.get('nickname')
                email = request.data.get('email', '')
                area = request.data.get('area')
                password = request.data.get('password')
                if not (username and nickname and area and password):
                    return_data = {}
                    if not username:
                        return_data['username'] = ['该字段不能为空。']
                    if not nickname:
                        return_data['nickname'] = ['该字段不能为空。']
                    if not area:
                        return_data['area'] = ['该字段不能为空。']
                    if not password:
                        return_data['password'] = ['该字段不能为空。']
                    return Response(return_data, 400)

                user = User.objects.filter(username=username)
                if user:
                    return Response({
                        'username': ['此用户名已被占用']
                    }, 400)
                area = Area.objects.filter(id=int(area))
                if not area:
                    return Response({
                        'area': ['Area 不存在']
                    }, 400)
                area = area[0]

                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                user_detail = UserDetail(nickname=nickname, area=area,
                                         user=user, user_type='admin')
                user_detail.save()

                return Response({
                    'username': username,
                    'nickname': nickname,
                    'area': {
                        'id': area.id,
                        'short_name': area.short_name,
                        'name': area.name
                    }
                }, 201)
            if request.user.userdetail.user_type == 'admin':
                return Response({
                    'user_type': ['您没有创建用户的权限']
                }, 403)
        # 用户自行注册
        username = request.data.get('username')
        nickname = request.data.get('nickname')
        email = request.data.get('email', '')
        school = request.data.get('school', '')
        college = request.data.get('college', '')
        major = request.data.get('major', '')
        team = request.data.get('team', '')
        area = request.data.get('area')
        password = request.data.get('password')
        code = request.data.get('code')
        if not (username and nickname and area and password and code):
            return_data = {}
            if not username:
                return_data['username'] = ['该字段不能为空。']
            if not nickname:
                return_data['nickname'] = ['该字段不能为空。']
            if not area:
                return_data['area'] = ['该字段不能为空。']
            if not password:
                return_data['password'] = ['该字段不能为空。']
            if not code:
                return_data['code'] = ['该字段不能为空。']
            return Response(return_data, 400)

        user = User.objects.filter(username=username)
        if user:
            return Response({
                'username': ['用户名已经被使用']
            }, 400)
        area = Area.objects.filter(id=int(area))
        if not area:
            return Response({
                'area': ['Area 不存在']
            }, 400)
        area = area[0]
        if area.code.strip() != code.strip():
            return Response({
                'code': ['邀请码错误']
            }, 400)

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        user_detail = UserDetail(nickname=nickname, area=area, user=user,
                                 school=school, college=college, major=major,
                                 team=team, user_type='user')
        user_detail.save()

        return Response({
            'username': username,
            'nickname': nickname,
            'area': {
                'id': area.id,
                'short_name': area.short_name,
                'name': area.name
            }
        }, 201)
