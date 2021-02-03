from django.shortcuts import render, redirect

def index(request):
    return redirect('/count')
    

def count(request):
    print("count++")
    return render(request, 'index.html')
    



