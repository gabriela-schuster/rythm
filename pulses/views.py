from django.shortcuts import render


def index(req):
	return render(req, 'pulses/home.html')


def dashboard(req):
	return render(req, 'pulses/dashboard.html')