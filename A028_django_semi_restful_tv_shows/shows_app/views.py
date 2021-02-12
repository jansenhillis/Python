from django.shortcuts import render, render

def index(request):
    return render(request, 'index.html')