from django.contrib.auth import authenticate
from django.contrib.auth.models import User, update_last_login
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from account.models import UserDetail
from account.oauth import get_access_token, get_user_info
from StepByStepBE.settings import client_id


@api_view(['GET'])
@permission_classes((AllowAny,))
def login(request):
    """ 通过 GitHub 的 oauth 系统登陆 """
    code = request.query_params.get('code')
    if code is None:
        return Response({
            'error': 'Please provide code',
            'redirect': f'https://github.com/login/oauth/authorize?client_id={client_id}'
        }, status=HTTP_400_BAD_REQUEST)
    access_token = get_access_token(code)
    user_info = get_user_info(access_token)

    username = user_info['login']
    email = user_info['email']
    password = 'password'  # 没有任何用处，也不会用这个密码来登陆
    user = authenticate(username=username, password=password)
    print(user_info)
    # 如果之前没有这个用户则创建
    if not user:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user_detail = UserDetail(
            user=user,
            github_id=user_info.get('id', ''),
            node_id=user_info.get('node_id', ''),
            avatar_url=user_info.get('avatar_url', ''),
            gravatar_id=user_info.get('gravatar_id', ''),
            url=user_info.get('url', ''),
            html_url=user_info.get('html_url', ''),
            name=user_info.get('name', ''),
            blog=user_info.get('blog', ''),
            location=user_info.get('location', ''),
            email=user_info.get('email', ''),
            bio=user_info.get('bio', ''),
        )
        user_detail.save()
    update_last_login(None, user)
    # 返回 Token
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key
    }, status=HTTP_200_OK)
