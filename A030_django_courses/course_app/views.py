from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
import re

def index(request):
    return render(request, 'index.html', {
        "courses": Course.objects.all(),
    })

def add_course(request):
    if request.method == "POST":
        # since request.POST is immutable for forms, create a custom dict to modify
        # before sending for validation
        postData = request.POST.copy()
        print (postData['name'])

        # Strip leading/trailing spaces, 
        # and all extra internal special chars except ! for both fields
        postData['name'] = re.sub("[^a-zA-Z0-9!]", " ", postData['name'].strip())
        postData['desc'] = re.sub("[^a-zA-Z0-9!]", " ", postData['desc'].strip())

        errors = Course.objects.validator(postData)

        if errors:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')
        else:
            name =  postData['name']
            desc = postData['desc']
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
        
