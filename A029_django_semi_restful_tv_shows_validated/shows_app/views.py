from django.shortcuts import render, redirect
from .models import TVShow
from datetime import datetime
from django.contrib import messages

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
        errors = TVShow.objects.validator(request.POST)

        print(errors)
        # Load errors to messages to display to user if any
        if errors: 
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('/shows/new')

        else:
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description']

            # check if the title already exists (exact match) - ignoring different cases for now
            result = TVShow.objects.filter(title=title)
            print ("result: ", result)
            if not result:
                show = TVShow.objects.create(title=title, network=network, release_date=release_date, description=description)

                if show:
                    return redirect('show_details', show.id)
            else:
                messages.error(request, "Show already exists!")
                return redirect('/shows/new')

def edit(request, show_id):
    show = TVShow.objects.get(id=show_id)

    # populate context with show object values
    return render(request, 'edit.html', {
        "show_id": show.id,
        "show_title": show.title,
        "show_network": show.network,
        "show_release_date": show.release_date.strftime("%Y-%m-%d"),
        "show_description": show.description,
    })

def update(request, show_id):
    if request.method == 'POST':
        errors = TVShow.objects.update_validator(request.POST, show_id)

        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('edit_view', show_id)
        else:
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description']

            show = TVShow.objects.get(id=show_id)

            if show:
                show.title = title
                show.network = network
                show.release_date = release_date
                show.description = description 
                show.save()

            return redirect('show_details', show_id)


def destroy(request, show_id):
    show = TVShow.objects.get(id=show_id)

    if show:
        show.delete()
    
    return redirect('/shows')
