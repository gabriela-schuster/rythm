from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    xp_total = models.PositiveIntegerField()

    def __str__(self):
        return str(self.xp_total)
