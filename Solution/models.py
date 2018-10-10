from django.contrib.auth.models import User
from django.db import models

from Problem.models import Problem


class Solution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)
    pid = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
    runid = models.CharField(max_length=128)
    result = models.CharField(max_length=128)
    time = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    language = models.CharField(max_length=128, blank=True)
    code_len = models.IntegerField(default=0)
    submission_time = models.DateTimeField(db_index=True, db_tablespace=True)

    class Meta:
        unique_together = ('source', 'runid',)

    def __str__(self):
        return '{} {} {}: {}'.format(self.source, self.user.userdetail.nickname,
                                     self.pid, self.result)
