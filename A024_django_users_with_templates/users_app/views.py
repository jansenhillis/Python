from django.shortcuts import render, redirect
from .models import Users

def index(request):
    context = {
        "users": Users.objects.all()
    }

    return render(request, 'index.html', context)

def add_user(request):
    if request.method == 'POST':
        first = request.POST['first_name'],
        last = request.POST['last_name'],
        email = request.POST['email_address'],
        age = request.POST['age']  

        Users.objects.create(first_name=first[0], last_name=last[0], email_address=email[0], age=age)        

        return redirect('/')
    else:
        return redirect('/')