from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["locations"] = request.POST["locations"]
        request.session["lang"] = request.POST["lang"]
        request.session["description"] = request.POST["description"]
    
        # return redirect(result(request))
        # result(request)
    
    return redirect('/')

def result(request):
    return render(request, "result.html")