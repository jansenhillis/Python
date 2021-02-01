from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Placeholder to later display a list of blogs.")

def new(request):
    return HttpResponse("Placeholder to display a new form to createa a new blog.") 

def show(request, number):
    return HttpResponse("placeholder to display blog number: " + str(number))

def edit(request, number):
    return HttpResponse("Placeholder to edit blog number: " + str(number))

def destroy(request, number):
    return HttpResponse("Placeholder to delete blog number: " + str(number))