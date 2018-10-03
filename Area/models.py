from django.db import models


class Area(models.Model):
    short_name = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)  # 邀请码

    content = models.TextField(max_length=10240, blank=True)  # 域的介绍

    def __str__(self):
        return self.short_name + ' ' + self.name
