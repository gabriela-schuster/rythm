from django.contrib.auth.models import User
from .models import Level
from django.db.models.signals import post_save


def createLevel(sender, instance, created, **kwargs):
	if created == True:
		user = instance
		level = Level.objects.create(
			user = user,
			xp_total = 0
		)

post_save.connect(createLevel, sender=User)
