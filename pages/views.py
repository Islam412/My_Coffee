from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1>Home page</h1>')


def about(request):
    return HttpResponse('<h1>About pages</h1>')

# def coffee(request):
#     return HttpResponse('<h1>Coffee shop</h1>')