from django.db import models


class Pulse(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	conclusion_time = models.IntegerField()
	concluded = models.BooleanField(default=False)
	   
	def __str__(self):
		return self.title
