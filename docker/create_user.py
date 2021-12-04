from django.contrib.auth.models import User

username = 'admin'
username_exists = User.objects.filter(username=username).exists()

if(username_exists):
	exit()

email = 'admin@admin.com'
password = 'admin'

user = User.objects.create_superuser(username, email, password)
user.save()
