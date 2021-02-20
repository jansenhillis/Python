from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)

        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/')
        else:
            # verify if user already exists
            user = User.objects.filter(email=request.POST['reg_email'])
            if not user:
                first = request.POST['first_name']
                last = request.POST['last_name']
                email = request.POST['reg_email']
                pw_hashed = bcrypt.hashpw(request.POST['reg_pw'].encode(), bcrypt.gensalt()).decode()

                user = User.objects.create(first=first, last=last, email=email, pw=pw_hashed)

                request.session['user_id'] = user.id
                return redirect('success')
            else: # existing user found
                messages.error(request, "Username already exists. Please try again.")
                return redirect('/')

def login_view(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        else:
            # verify if user exists
            user = User.objects.filter(email=request.POST['login_email'])

            # verify their password hashes match

            request.session['user_id'] = user[0].id
            return redirect('success')


def logout(request):
    del request.session['user_id']
    return redirect('/')

def success_view(request):
    if request.session['user_id']:
        user = User.objects.filter(id=request.session['user_id'])

    return render(request, 'account.html', {
        "first_name": user[0].first
    })