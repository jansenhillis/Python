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

def new(request):
    return render(request, 'add.html')

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']

        show = TVShow.objects.create(title=title, network=network, release_date=release_date, description=description)

        if show:
            return redirect('show_details', show.id)
        else:
            return redirect('/')
    else:
        return redirect('/')

def edit(request, show_id):
    show = TVShow.objects.get(id=show_id)

    # populate context with show object
    return render(request, 'edit.html', {
        "show": show
    })

def update(request, show_id):
    if request.method == 'POST':
        pass
    else:
        return redirect('/')