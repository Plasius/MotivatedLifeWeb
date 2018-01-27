from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import Http404
from django.db.models import Q

# Create your views here.
def post_create(request):
    if not request.user.is_staff:
        raise Http404("User not staff")


    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'blog/post_form.html', context)

def post_detail(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    if instance.draft and not request.user.is_staff:
        raise Http404('Article not found')
    context= {
        'obj' : instance,
        'staff' : request.user.is_staff
    }

    return render(request, 'blog/post_detail.html', context)

def post_list(request):
    if request.user.is_staff:
        queryset= Post.objects.all()
    else:
        queryset= Post.objects.filter(draft=False).filter(published__lte = timezone.now()).all()

    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'object_list' : posts,
        'staff' : request.user.is_staff,
        'paratlan' : range(1,10,2)
    }
    return render(request, 'blog/post_list.html', context)



def post_update(request, pk=None):
    if not request.user.is_staff:
        raise Http404("User not staff")
    instance = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance= instance)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'instance':instance,
        'form': form
    }
    return render(request, 'blog/post_form.html', context)

def post_delete(request, pk=None):
    if not request.user.is_staff:
        raise Http404("User not staff")
    instance = get_object_or_404(Post, id=pk)
    instance.delete()
    return redirect('bloglist')
