from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post
import logging

    # f Data
# posts = [
#         {'id':1, 'title': 'Post 1', 'content': 'Content of Post 1', 'category': 'Sports'},
#         {'id':2, 'title': 'Post 2', 'content': 'Content of Post 2', 'category': 'Science'},
#         {'id':3, 'title': 'Post 3', 'content': 'Content of Post 3', 'category': 'Politics'},
#         {'id':4, 'title': 'Post 4', 'content': 'Content of Post 4', 'category': 'Geography'},
#         {'id':5, 'title': 'Post 5', 'content': 'Content of Post 5', 'category': 'Film Industry'},
#         {'id':6, 'title': 'Post 6', 'content': 'Content of Post 6', 'category': 'Education'},
#     ]

# Create your views here.
def index(request):
    blog_title = "Blog Post"
    blog_head = "My Blog"
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'blog_title':blog_title, "blog_head":blog_head, 'posts' : posts})

def detail(request, post_id):
    Post = next((item for item in posts if item['id'] == int(post_id)), None)
    logger = logging.getLogger("Testing")
    logger.debug(f'post variable is {Post}')
    return render(request, 'blog/detail.html', {'post':Post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_url_page'))

def new_url_view(request):
    return HttpResponse("<h2>This is new URL</h2>")
