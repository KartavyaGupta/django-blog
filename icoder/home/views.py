import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import post
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')

def search(request):
    query=request.GET['query']
    allposts_title= post.objects.filter(title__icontains=query)
    allposts_content= post.objects.filter(content__icontains=query)
    records = (allposts_title | allposts_content).distinct()
    print(records)

    params={'allposts': records}
    return render(request, 'home/search.html', params)



def contact_view(request):

    if request.method == 'POST':

        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        content1 = request.POST.get('content')
        timestamp1 = datetime.now()

        if len(name1) != 0 and len(name1) != 0 and len(name1) != 0 and len(name1) != 0:
            messages.success(request, 'message sent successfully.')
            contact1 = contact(name=name1, email=email1, phone=phone1,
                               content=content1, timestamp=timestamp1)
            print(name1, email1, phone1, content1, timestamp1)

            contact1.save()
        else:
            messages.warning(
                request, 'message not sent. please fill the form properly')
    return render(request, 'home/contact.html')


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if len(username) < 2 or len(firstname) < 2 or len(lastname) < 2 or len(email) < 2:
            messages.warning(
                request, 'username, firstname, lastname and email should be of more than 2 characters.')
        else:

            user_new = User.objects.create_user(
                username=username, first_name=firstname, last_name=lastname, email=email, password=pass1)
            messages.success(request, 'signup completed successfully.')

    else:
        messages.warning(request, 'sign up failed.')

    return redirect('home')


def handlelogin(request):
    print(vars(request))
    if request.method == 'POST':
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')
        print(username, password)
        user = authenticate(username=username, password=password)
        print("user detected")
        if user is not None:
            messages.success(request, 'login succesful')
            login(request, user)
        else:
            messages.warning(request, 'wrong username or password')
    else:
        messages.warning(request, 'login failed.')
    return redirect('home')


def handlelogout(request):
    print("logout")
    logout(request)
    messages.success(request, 'logout successful')
    return redirect('home')
