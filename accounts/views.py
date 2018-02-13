from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

# Create your views here.

# /register
def register_view(request, passError=False, existsError=False):
	c= {}
	c.update(csrf(request))
	c['title']= 'Register'

	if existsError:
		c['existsError'] = True
	elif passError:
		c['passError'] = True

	return render(request, 'accounts/register.html', c)

# /login
def login_view(request, error = False):
	c= {}
	c.update(csrf(request))
	c['title']= 'Login'

	if error:
		c['error'] = True

	return render(request, 'accounts/login.html', c)

# /auth -form
def auth_view(request, onsuccess='/dashboard/'):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return login_view(request, True)

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()

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
	try:
		if validate_password(post['password']) == None:
			if not user_email_exists(post['email']) and not user_name_exists(post['username']):
				create_user(username=post['username'], email=post['email'], password=post['password'])
				return auth_view(request)
			else:
				return register_view(request, existsError = True)
	except Exception as e:
		return register_view(request, passError = True)

# /logout
def logout_view(request):
	logout(request)
	return redirect('/')
