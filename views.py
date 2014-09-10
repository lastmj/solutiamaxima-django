from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from forms import MyRegistrationForm

def login_view(request):
	context = {}
	return render(request, 'login.html', context)
	
def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('publicworkspace:index'))
	else:
		context = {}
		return render(request, 'login.html', context)

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('publicworkspace:index'))
	
def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if request.POST['passkey'] == 'tester555':
			if form.is_valid():
				form.save()
				newUser = authenticate(username=request.POST['username'], password=request.POST['password1'])
				login(request, newUser)
				return HttpResponseRedirect(reverse('views.tutorial'))
				
	context = {'form':MyRegistrationForm()}
	return render(request, 'register.html', context)
	
def universal_terms(request):
	context = {}
	return render(request, 'universal-terms.html', context)

@login_required
def tutorial(request):
	context = {}
	return render(request, 'tutorial.html', context)
