from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process_money(request):
    return redirect('/')