from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.GET:
        return redirect('/')
    elif request.POST:
        request.session["name"] = request.POST["name"]
        request.session["locations"] = request.POST["locations"]
        request.session["lang"] = request.POST["lang"]
        request.session["description"] = request.POST["description"]
        
        return render(request, 'result.html')
    else:
        return redirect('/')

