from django.contrib.auth.models import User
from django.db import models


class Source(models.Model):
    """ OJ 平台 """
    name = models.CharField(max_length=1024)
    url = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserBindSource(models.Model):
    """ 用户与 OJ 平台的绑定 """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    username = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.source.name}: {self.username}'
