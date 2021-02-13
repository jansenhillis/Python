from django.shortcuts import render, render, redirect
from .models import TVShow
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "tvshows": TVShow.objects.all()
    }
    return render(request, 'index.html', context)