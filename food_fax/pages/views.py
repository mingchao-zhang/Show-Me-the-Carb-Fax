from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def demo(request):
    return render(request, 'pages/demo.html')

def sign_in(request):
    return render(request, 'pages/sign_in.html')

def contact(request):
    return render(request, 'pages/contact.html')