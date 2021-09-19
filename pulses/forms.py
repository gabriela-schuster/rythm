from django.db.models import fields
from .models import Pulse
from django import forms


class Pulseform(forms.ModelForm):
	class Meta:
		model = Pulse
		fields = ['title', 'description', 'conclusion_time']

	# def __init__(self, *args, **kwargs):
	# 	super(Pulseform).__init__(*args, **kwargs)
	# 	for name, field in self.fields.items():
	# 		field.widget.attrs.update({'class': 'input'})
