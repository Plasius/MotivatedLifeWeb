from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from .models import IdentityProfile
from django.http import HttpResponse

#/identity/me
@login_required(login_url='/account/login')
def main(request):
    try:
        identity = IdentityProfile.objects.get(user=request.user)
    except IdentityProfile.DoesNotExist:
        identity = None

    if not identity:
        return redirect('/identity/create_identity')
    else:
        return redirect('/identity/me')

#/identity/create_identity
@login_required(login_url='/account/login')
def create_identity_view(request):
    return HttpResponse('create your identity here')

#/identity/me
@login_required(login_url='/account/login')
def my_identity_view(request):
    return HttpResponse('My age is:'+ str(IdentityProfile.objects.get(user=request.user).age))
