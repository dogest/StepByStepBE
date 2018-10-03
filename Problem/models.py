from django.db import models


class Problem(models.Model):
    name = models.CharField(max_length=128)
    pid = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
    url = models.CharField(max_length=512)

    def __str__(self):
        return '{}: {} {}'.format(self.source, self.pid, self.name)
