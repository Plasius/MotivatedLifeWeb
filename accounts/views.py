from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def register_view(request):
	c= {}
	c.update(csrf(request))
	c['title']= 'Register'
	return render(request, 'accounts/register.html', c)

def login_view(request):
	c= {}
	c.update(csrf(request))
	c['title']= 'Login'
	return render(request, 'accounts/login.html', c)
	
def auth_view(request, onsuccess='/dashboard/', onfail='/fail'):
    user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
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
	
def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True
	
def signup_view(request):
	post = request.POST
	if not user_exists(post['email']):
		user = create_user(username=post['email'], email=post['email'], password=post['password'])
		return auth_view(request)
	else:
		return redirect("/account/login/")
		
def logout_view(request):
	logout(request)
	return redirect('/')
		