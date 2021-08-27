from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html' )

def register(request):
    return render(request, 'register.html')

def signin(request):
    return render(request, 'signin.html')