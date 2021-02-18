from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def index(request):
    return render(request, 'index.html', {
        "courses": Course.objects.all(),
    })

def add_course(request):
    if request.method == "POST":
        errors = Course.objects.validator(request.POST)
        print(errors)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')
        else:
            name = request.POST['name']
            desc = request.POST['desc']
            course = Course.objects.create(name=name, desc=desc)            
            
            return redirect('/')
    else:
        return redirect('/')
            
def destroy(request, course_id):
    if request.method == "GET":
        course = Course.objects.get(id=course_id)

        if course:
            return render(request, 'confirm_delete.html', {
                "course": course,
            })

    if request.method == "POST":
        course = Course.objects.get(id=course_id)

        # if a course was found
        if course:
            course.delete()

        return redirect('/')
        
