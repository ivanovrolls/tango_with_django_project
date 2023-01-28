from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! About page: " + '<a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse("Rango says here is the about page. Index page: " + '<a href="/rango/">Index</a>')