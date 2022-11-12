from asyncio.windows_events import NULL
from contextlib import redirect_stderr
from datetime import datetime
from email import message
from email.policy import default
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import post, comment
from django.utils.timezone import now
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.


def bloghome(request):
    allposts = post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'blog/bloghome.html', context)


def blogpost(request, slug):
    post1 = post.objects.filter(slug=slug).first()
    comments1 = comment.objects.filter(blogpost=post1,blogparent = None)
    replies1 = comment.objects.filter(blogpost=post1).exclude(blogparent = None)

    post1.views=post1.views+1
    post1.save()

    replydict={}
    for reply in replies1:
        if reply.blogparent.blogsno not in replydict:
            replydict[reply.blogparent.blogsno]=[reply]
        else:
            replydict[reply.blogparent.blogsno].append(reply)
 

    log_user = request.user
    context = {'post': post1, 'comments': comments1, 'log_user': log_user,'replydict':replydict}

    return render(request, 'blog/blogpost.html', context)


def postcomment(request):

    if request.method == 'POST':
        postsno = request.POST.get('postsno')
        parentcommentsno = request.POST.get('parentcommentsno')
        user1 = request.user
        post1 = post.objects.filter(sno=postsno).first()
        comment1 = request.POST.get('usercomment')
        if parentcommentsno == "":
            blogcomment1 = comment(blogcomment=comment1,
                                   bloguser=user1, blogpost=post1)
            blogcomment1.save()
        else:
            parent_of_reply = comment.objects.get(blogsno=parentcommentsno)
            reply1 = comment(blogcomment=comment1, bloguser=user1,
                             blogpost=post1, blogparent=parent_of_reply)
            reply1.save()

        messages.success(request, 'message posted')
        return redirect(f"/blog/{post1.slug}")

    else:
        return redirect("/")
