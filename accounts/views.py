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
        if 'lname' in request.POST: last_name = request.POST['lname']
        if 'address' in request.POST: address = request.POST['address']
        if 'address2' in request.POST: address2 = request.POST['address2']
        if 'city' in request.POST: city = request.POST['city']
        if 'state' in request.POST: state = request.POST['state']
        if 'zip' in request.POST: zip_number = request.POST['zip']
        if 'email' in request.POST: email = request.POST['email']
        if 'user' in request.POST: username = request.POST['user']
        if 'password' in request.POST: password = request.POST['password']
        if 'terms' in request.POST: terms = request.POST['terms']

        return redirect('signup')
    else:
        return render(request , 'accounts/signup.html')


def profile(request):
    if request.method == 'POST' and 'btnsave' in request.POST:
        messages.info(request,'This is POST and btnsave')
        return redirect('profile')
    else:
        return render(request,'accounts/profile.html')