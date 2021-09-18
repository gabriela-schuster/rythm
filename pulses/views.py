from typing import Collection
from django.shortcuts import render, redirect
from .models import Pulse
from .forms import Pulseform, PulseformAll


def index(req):
	return render(req, 'pulses/home.html')


def dashboard(req):
	user = req.user
	user_level = user.level_set.all()
	concluded = Pulse.objects.all().filter(player=user).filter(concluded=True)
	three_pulses = Pulse.objects.all().filter(player=user).filter(
		concluded=True)[len(concluded) - 3:]
	try:
		not_concluded = Pulse.objects.all().filter(concluded=False).latest('title')
	except:
		not_concluded = None

	context = {
		'three_pulses': three_pulses,
		'concluded': len(concluded),
		'not_concluded': not_concluded,
		'user': user,
		'user_level': user_level,
	}

	if req.method == 'POST':
		form = PulseformAll(req.POST, instance=not_concluded)
		form.save()
		return redirect('dashboard')

	return render(req, 'pulses/dashboard.html', context)


def add_pulse(req):
	# user = req.user
	form = Pulseform()

	if req.method == 'POST':
		form = Pulseform(req.POST)
		if form.is_valid:
			form.save()
			return redirect('dashboard')

	return render(req, 'pulses/add_pulse.html', {'form': form})
