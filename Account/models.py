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

    # if user_type == 'admin' or user_type == 'user'
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
