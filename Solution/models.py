from django.contrib.auth.models import User
from django.db import models

from Problem.models import Problem


class Solution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    source = models.CharField(max_length=128)
    runid = models.CharField(max_length=128)
    result = models.CharField(max_length=128)
    time = models.IntegerField()
    memory = models.IntegerField()
    language = models.CharField(max_length=128)
    code_len = models.IntegerField()
    submission_time = models.DateTimeField(db_index=True, db_tablespace=True)
