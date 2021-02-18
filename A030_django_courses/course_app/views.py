from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def index(request):
    return render(request, 'index.html', {
        "courses": Course.objects.all()
    })

def add_course(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        
        if errors:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')
        else:
            name = request.POST['name']
            desc = request.POST['desc']
            course = Course.objects.create(name=name, desc=desc)            
            
            return redirect('/')
            
def destroy(request, course_id):
    pass