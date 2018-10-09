from django.contrib.auth.models import User
from django.db import models

from Area.models import Area

user_types = (
    ('root', '总管理员'),
    ('admin', '域管理员'),
    ('user', '用户')
)


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=128)
    user_type = models.CharField(max_length=128, choices=user_types)

    # 在学校的信息（如果有的话）
    school = models.CharField(max_length=128, blank=True)  # 学校
    college = models.CharField(max_length=128, blank=True)  # 学院
    major = models.CharField(max_length=128, blank=True)  # 系
    team = models.CharField(max_length=128, blank=True)  # 班级 / 组

    # if user_type == 'admin' or user_type == 'user'
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nickname


class UserOJBind(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
