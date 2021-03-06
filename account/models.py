from django.contrib.auth.models import User
from django.db import models


class UserDetail(models.Model):
    """ 从 GitHub 获取到的用户信息 """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=1024, primary_key=True)
    github_id = models.IntegerField()
    node_id = models.CharField(max_length=1024, blank=True, null=True)
    avatar_url = models.CharField(max_length=1024, blank=True, null=True)
    gravatar_id = models.CharField(max_length=1024, blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    html_url = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    blog = models.CharField(max_length=1024, blank=True, null=True)
    location = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    bio = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.user.username
