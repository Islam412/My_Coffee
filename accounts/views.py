from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def signin(request):
    if request.GET:
        messages.info(request,'testing messages 1')
    return render(request , 'accounts/signin.html')


def signup(request):
    return render(request , 'accounts/signup.html')


def profile(request):
    return render(request,'accounts/profile.html')