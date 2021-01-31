from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Placeholder to later display a list of blogs.")

def new(request):
    return HttpResponse("Placeholder to display a new form to createa a new blog.") 

def show(request, number):
    