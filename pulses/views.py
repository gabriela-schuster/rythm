from django.shortcuts import render
from .models import Pulse
from .forms import Pulseform


def index(req):
	return render(req, 'pulses/home.html')


def dashboard(req):
	three_pulses = Pulse.objects.all()[:3]
	concluded = Pulse.objects.all().filter(concluded=True)
	not_concluded = Pulse.objects.all().filter(concluded=False).latest('title')
	context = {
		'three_pulses': three_pulses,
		'concluded': len(concluded),
		'not_concluded': not_concluded,

	}
	return render(req, 'pulses/dashboard.html', context)
		

def add_pulse(req):
	form = Pulseform()
	return render(req, 'pulses/add_pulse.html', {form})
