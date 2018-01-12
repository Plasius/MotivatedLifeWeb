from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import QuoteProfile, Quote

import random
import datetime

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
	profile = QuoteProfile.objects.filter(user= request.user).get()

	#already a user
	if profile.updated == datetime.date.today():
		q = Quote.objects.filter(day = profile.currentDay).get()
	else:
		if profile.progress > 0:
			profile.seenCount +=1
			profile.seen += ' '+ str(profile.currentDay)

		#new or old user
		profile.updated = datetime.datetime.now().strftime("%Y-%m-%d")
		profile.progress += 1

		if profile.progress == 151:
			profile.progress = 1
			profile.seenCount = 0
			profile.seen = ''

		seen = [int(x) for x in profile.seen.split()]
		unseen = range(1, 151)
		unseen = list(set(unseen) - set(seen))

		day = random.randint(a=0, b=len(unseen))+1
		q = Quote.objects.filter(day = day).get()
		profile.currentDay = q.day

		profile.save()
	return render(request, 'daily/dashboard.html', {'title':'Dashboard', 'progress': profile.progress, 'quote': q.name})
