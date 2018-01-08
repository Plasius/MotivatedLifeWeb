from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import QuoteProfile

# Create your views here.
def main(request):
	if request.user.is_authenticated:
		return redirect('/dashboard/')

	c= {}
	c.update(csrf(request))
	c['title']= 'Motivated life'
	return render(request, 'daily/home.html', c)


@login_required(login_url='/account/login')
def dashboard(request):
	#get the progress of a user
	profile= QuoteProfile.objects.filter(user= request.user).get()
	return render(request, 'daily/dashboard.html', {'title':'Dashboard', 'progress': profile.progress})
