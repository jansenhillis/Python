from django.shortcuts import render, redirect

def index(request):
    return redirect('/random_word')
    
def random_word(request):
    # if the key doesn't exist, this is first run. Create it
    if 'count' not in request.session.keys():
        request.session['count'] = 0

    # get new random word

    # increment counter 
    request.session['count'] += 1

    return render(request, 'index.html')