from django.shortcuts import render, render, redirect

def index(request):
    return redirect('/shows')

def shows(request):
    return render(request, 'index.html')