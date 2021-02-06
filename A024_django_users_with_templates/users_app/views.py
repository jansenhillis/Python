from django.shortcuts import render
from .models import Users

def index(request):
    context = {
        "users": Users.objects.all()
    }

    return render(request, 'index.html', context)