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
            if user:
                # verify password hashes match
                if bcrypt.checkpw(request.POST['login_pw'].encode(), user[0].pw.encode()):
                    # matched, drop the session variable
                    request.session['user_id'] = user[0].id
                    return redirect('success')
                else:
                    messages.error(request, "Password incorrect. Try again.")
                    return redirect('/')
            else:
                messages.error(request, "User email not found.")
                return redirect('/')



def logout(request):
    del request.session['user_id']
    return redirect('/')

def success_view(request):
    # check to see if the userid has been placed into the session
    if 'user_id' in request.session:
        user = User.objects.filter(id=request.session['user_id'])

        return render(request, 'account.html', {
            "user": user[0]
        })
    else:
        return redirect('/')