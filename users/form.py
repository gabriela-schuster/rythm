from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

 
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	# def __init__(self, *args, **kwargs):
	# 	super(Pulseform).__init__(*args, **kwargs)
	# 	for name, field in self.fields.items():
	# 		field.widget.attrs.update({'class': 'input'})
