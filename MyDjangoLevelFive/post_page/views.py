from django.shortcuts import render
from post_page.models import Post
from post_page.forms import PostForm
# Create your views here.

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

def post(request):
    post_list = Post.objects.order_by('title')
    post_dict = post_list

    return render(request, 'post_page/post.html', {'posts':post_dict})

def create_post(request):
    if request.method == 'POST':
        my_post = PostForm(request.POST)

        if my_post.is_valid():
            mypost = my_post.save(commit=True)
            mypost.save()

            return HttpResponseRedirect(reverse('post'))
        else:
            return HttpResponse('Invalid Post')

    else:
        my_post = PostForm()

    return render(request, 'post_page/create_post.html', {'my_post':my_post})