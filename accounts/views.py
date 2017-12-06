from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# /register
def register_view(request):
	c= {}
	c.update(csrf(request))
	c['title']= 'Register'
	return render(request, 'accounts/register.html', c)

# /login
def login_view(request):
	c= {}
	c.update(csrf(request))
	c['title']= 'Login'
	return render(request, 'accounts/login.html', c)

# /auth -form
def auth_view(request, onsuccess='/dashboard/', onfail='/fail'):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_email_exists(email):
    user_count = User.objects.filter(username=email).count()
    if user_count == 0:
        return False
    return True

def user_name_exists(name):
    user_count = User.objects.filter(username=name).count()
    if user_count == 0:
        return False
    return True

# /signup -form
def signup_view(request):
	post = request.POST
	if not user_email_exists(post['email']) and not user_name_exists(post['username']):
		user = create_user(username=post['username'], email=post['email'], password=post['password'])
		return auth_view(request)
	else:
		return redirect("/account/login/")

# /logout
def logout_view(request):
	logout(request)
	return redirect('/')
