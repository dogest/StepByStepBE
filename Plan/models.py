from django.contrib.auth.models import User
from django.db import models

from Area.models import Area


class Plan(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class PlanUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.plan.name, self.user.userdetail.nickname)


class PlanProblem(models.Model):
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)
    content = models.TextField(max_length=102400)

    def __str__(self):
        return self.plan.name
