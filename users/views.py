from django.shortcuts import redirect, render
from .form import UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages, auth


def create_user(req):
	form = UserForm()
	context = {
		'form': form
	}

	if req.method == 'POST':
		user = UserForm(req.POST)
		if user.is_valid():
			user.save()

			username = req.POST['username']
			password = req.POST['password1']

			user_authenticated = auth.authenticate(req, username=username, password=password)
			auth.login(req, user_authenticated)

			return redirect('dashboard')
		else:
			messages.add_message(req, messages.ERROR, f'{user.errors}')

	return render(req, 'users/create_user.html', context)


def login(req):
	if req.user.is_authenticated:
		return redirect('dashboard')

	if req.method == 'POST':
		username = req.POST['username']
		password = req.POST['password']

		user = authenticate(req, username=username, password=password)
		if user != None:
			auth.login(req, user)
			return redirect('dashboard')
		else:
			messages.error(req, 'usuário ou senha incorretos')

	return render(req, 'users/login.html')


def logout_user(req):
	logout(req)
	return redirect('index')