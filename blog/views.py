from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        form = PostForm()
    return render(request, 'blog/templates/post_edit.html', {'form': form, 'posts': posts})

