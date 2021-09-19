from django.db import models
from django.contrib.auth.models import User


class Pulse(models.Model):
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    conclusion_time = models.IntegerField()
    concluded = models.BooleanField(default=False)

    def __str__(self):
        return self.title

