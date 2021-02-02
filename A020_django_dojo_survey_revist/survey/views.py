from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.GET:
        return redirect('/')
    elif request.POST:
        context = {
            "name": request.POST["name"],
            "locations": request.POST["locations"],
            "lang": request.POST["lang"],
            "description" : request.POST["description"],
        }

        return render(request, 'result.html', context)

