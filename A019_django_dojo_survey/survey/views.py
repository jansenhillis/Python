from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def result(request):
    return HttpResponse(request)