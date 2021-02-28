from django.shortcuts import render, redirect
from .models import User
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
            user = User.objects.register_user(request)
            if user:
                request.session['user_id'] = user.id
                return redirect('success')
            else: # existing user found
                messages.error(request, "Username/email already exists. Please try again.")
                return redirect('/')

def login_view(request):
    if request.method == "POST":
        
        user = User.objects.login_user(request)
        if user:
            request.session['user_id'] = user[0].id
            return redirect('success')
        else:
            messages.error(request, "Email/Password incorrect. Try again.")
            return redirect('/')
            
def logout(request):
    request.session.clear()
    return redirect('/')

def success_view(request):
    # check to see if the userid has been placed into the session
    if 'user_id' in request.session:
        return redirect('/books')
    else:
        return redirect('/')