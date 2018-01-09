from django.contrib import messages
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def post_create(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        messages.success(request, 'Succesfully Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Succesfully Created')
    context = {
        'form': form
    }
    return render(request, 'blog/post_form.html', context)

def post_detail(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    context= { 'instance' : instance}

    return render(request, 'blog/post_detail.html', context)

def post_list(request):
    queryset= Post.objects.all()
    context = {
        'object_list' : queryset,
    }
    return render(request, 'blog/base.html', context)

def post_update(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance= instance)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        messages.success(request, 'Succesfully updated')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'instance':instance,
        'form': form
    }
    return render(request, 'blog/post_form.html', context)

def post_delete(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    instance.delete()
    messages.success(request, 'Succesfully updated')
    return redirect('bloglist')
