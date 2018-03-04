from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from .models import IdentityProfile
from django.http import HttpResponse
from django.template.context_processors import csrf

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
    try:
        identity = IdentityProfile.objects.get(user=request.user)
    except IdentityProfile.DoesNotExist:
        identity = None
    if identity:
        return redirect('/identity/me')

    ifile = open('identity/res/identity.txt', 'r')
    message = '<div class=\'section\'>'
    argN = 1
    for line in ifile:
        if line == 'break\n':
            message+="</div><div class='section'>"
        elif line == 'end\n':
            message+='<br><button id="butt" style="background-color:#CDDC39;color:black;" class="btn btn-lg btn-block" type="submit" name="submit" value="submit-value">This is me</button>'
            message+='</div>'
        else:
            for word in line.split():
                if word.startswith('arg'):
                    line = line.replace('arg'+str(argN), '<input class="textspace" required name=\''+ 'arg'+str(argN) +'\'></input>')
                    argN += 1

            message += line + '<br>'
    context = {'formhtml' : message}
    context.update(csrf(request))
    return render(request, 'identity/identity.html', context)

#/identity/me
@login_required(login_url='/account/login')
def my_identity_view(request):
    try:
        identity = IdentityProfile.objects.get(user=request.user)
    except IdentityProfile.DoesNotExist:
        identity = None

    if not identity:
        return redirect('/identity/create_identity')
    else:
        try:
            values = IdentityProfile.objects.get(user=request.user).values.split('0')
        except IdentityProfile.DoesNotExist:
            return redirect('/fail')

        ifile = open('identity/res/identity.txt', 'r')
        message = '<div class=\'section\'>'
        argN = 1
        for line in ifile:
            if line == 'break\n':
                message+="</div><div class='section'>"
            elif line == 'end\n':
                message+='</div>'
            else:
                for word in line.split():
                    if word.startswith('arg'):
                        line = line.replace('arg'+str(argN), values[argN-1])
                        argN += 1

                message += line + '<br>'
        context = {'formhtml' : message}
        context.update(csrf(request))
        return render(request, 'identity/identity.html', context)


#/identity/make_identity
@login_required(login_url='/accout/login')
def make_identity_view(request):
    if not request.POST:
        redirect('/fail')
    post= request.POST

    values = []
    argN = 11 #-1
    for arg in range(1, argN):
        values.append(post['arg'+str(arg)])

    identity = IdentityProfile(user = request.user, values = '0'.join(values))
    identity.save()

    return redirect('/identity/me')
