from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Comment
from .forms import CommentForm

import logging

logger = logging.getLogger(__name__)

def get_post_list(page=1, tag_slug=None):
    posts = Post.objects.filter(status="published").all()

    paginator = Paginator(posts, 5) 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
    return posts,page

def homepage(request):
    page = request.GET.get('page')
    posts,page = get_post_list(page)

    best_posts = Post.objects.filter(status="published").all()[:3]

    return render(request, 'home.html',{'posts' : posts, 'best_posts':best_posts, 'page':page})

def about_me(request):
    return render(request, 'about_me.html')

def post_list(request, tag_slug=None):
    page = request.GET.get('page')
    posts,page = get_post_list(page,tag_slug=tag_slug)

    return render(request, 'post/post_list.html',{'posts' : posts, 'page':page})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
     status='published',publish__year=year,publish__month=month,publish__day=day, slug=slug)
    
    if request.method=='POST':
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            new_comment = Comment()

            new_comment.author = commentForm.cleaned_data['author']
            new_comment.body = commentForm.cleaned_data['body']
            new_comment.post = post
            if 'comment_parent' in request.POST: 
                if request.POST['comment_parent']:
                    comment_parent_t = Comment.objects.get(pk = int(request.POST['comment_parent']))
                    new_comment.comment_parent = comment_parent_t

            new_comment.save()
        return HttpResponseRedirect(request.path_info)
    else:
        commentForm = CommentForm()
    
    comments = Comment.objects.filter(post=post)
    return render(request,'post/detail.html',
        {'post': post, 'comments':comments, 'form':commentForm})
