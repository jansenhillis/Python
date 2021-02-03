from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["locations"] = request.POST["locations"]
        request.session["lang"] = request.POST["lang"]
        request.session["description"] = request.POST["description"]
    
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'result.html')