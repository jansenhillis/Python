from django.shortcuts import render, redirect

def index(request):
    return redirect('/count')
    

def count(request):
    # if the key doesn't exist, this is first run. Create it
    if 'count' not in request.session.keys():
        request.session['count'] = 0
    
    request.session['count'] += 1
    return render(request, 'index.html')
    



