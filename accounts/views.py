from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
import re



def signin(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:
        messages.info(request,'This is POST and btnlogin')
        return redirect('signin')
    else:
        return render(request , 'accounts/signin.html')


def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
        #variables for fieles
        frist_name = None
        last_name = None
        address = None
        address2 = None
        city = None
        state = None
        zip_number = None
        email = None
        username = None
        password = None
        terms = None
        
        #GET value from form
        if 'fname' in request.POST: frist_name = request.POST['fname']
        else: messages.error(request,'Error in frist name')
        if 'lname' in request.POST: last_name = request.POST['lname']
        else: messages.error(request,'Error in last name')
        if 'address' in request.POST: address = request.POST['address']
        else: messages.error(request,'Error in  address')
        if 'address2' in request.POST: address2 = request.POST['address2']
        else: messages.error(request,'Error in  address 2')
        if 'city' in request.POST: city = request.POST['city']
        else: messages.error(request,'Error in  city')
        if 'state' in request.POST: state = request.POST['state']
        else: messages.error(request,'Error in  state')
        if 'zip' in request.POST: zip_number = request.POST['zip']
        else: messages.error(request,'Error in  zip number')
        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,'Error in  email')
        if 'user' in request.POST: username = request.POST['user']
        else: messages.error(request,'Error in  user name')
        if 'password' in request.POST: password = request.POST['password']
        else: messages.error(request,'Error in  password')
        if 'terms' in request.POST: terms = request.POST['terms']
        
        #check all values
        if frist_name and last_name and address and address2 and city and state and zip_number and email and username and password:
            if terms == 'on':
                #check if username
                if User.objects.filter(username=username).exists():
                    messages.error(request,'User name is taken')
                else:
                    pass
            else:
                message.error(request,'You must agree to the terms')
        else:
            messages.error(request,'check empty fields')
        return redirect('signup')
    else:
        return render(request , 'accounts/signup.html')


def profile(request):
    if request.method == 'POST' and 'btnsave' in request.POST:
        messages.info(request,'This is POST and btnsave')
        return redirect('profile')
    else:
        return render(request,'accounts/profile.html')