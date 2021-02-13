from django.shortcuts import render, render, redirect
from .models import TVShow

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "tvshows": TVShow.objects.all()
    }
    return render(request, 'index.html', context)

def show_description(request, show_id):
    # lookup show
    show = TVShow.objects.get(id=show_id)

    # populate context with show object
    return render(request, 'show.html', {
        "show": show
    })