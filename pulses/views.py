from typing import Collection
from django.shortcuts import render, redirect
from .models import Pulse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Pulseform


def index(req):
	if req.user:
		return redirect('dashboard')
	else:
		return render(req, 'pulses/home.html')


@login_required(login_url='login')
def dashboard(req):
	user = req.user
	user_level = user.level_set.get(user=user)

	concluded = Pulse.objects.all().filter(player=user).filter(concluded=True)
	try:
		three_pulses = Pulse.objects.all().filter(player=user).filter(
			concluded=True)

		if len(three_pulses) == 1 or len(three_pulses) == 2:
			three_pulses = three_pulses
		else:
			three_pulses = three_pulses[len(concluded) - 3:]
	except:
		# if user didn't complete three pulses
		three_pulses = None

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
		# creating a new Pulse object from hidden form, and deleting the
		# not_concluded
		title = req.POST.get('title')
		description = req.POST.get('description')
		conclusion_time = req.POST.get('conclusion_time')
		player = user

		pulse = Pulse.objects.create(player=player, title=title, description=description, conclusion_time=conclusion_time, concluded=True)

		if not_concluded:
			not_concluded.delete()

		pulse.save()

		actual_xp = int(conclusion_time) + int(user_level.xp_total)
		user_level.xp_total = actual_xp
		user_level.save()

		return redirect('dashboard')

	return render(req, 'pulses/dashboard.html', context)


@login_required(login_url='login')
def add_pulse(req):
	# user = req.user
	form = Pulseform()

	if req.method == 'POST':
		form = Pulseform(req.POST)
		if form.is_valid:
			form.save()
			return redirect('dashboard')

	return render(req, 'pulses/add_pulse.html', {'form': form})


def ranking(req):
	players = User.objects.all()
	context = {'players': players}
	return render(req, 'pulses/ranking.html', context)
