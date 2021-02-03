from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    for item in request.session.keys():
        print(item)
    return redirect('/random_word')
    
def random_word(request):
    # If the key doesn't exist, this is first run. 
    # init counter and word keys
    if 'count' not in request.session.keys():
        request.session['count'] = 0
        request.session['random_word'] = '0123456789ABCD'

    # load a new random word into the session
    request.session['random_word'] = get_random_str()

    # increment counter 
    request.session['count'] += 1

    return render(request, 'index.html')

# Source a random 14 char string
def get_random_str():
    return get_random_string(length=14)

# Reset method to reset both counters to initial values
def reset(request):
    if 'count' in request.session.keys():
        request.session['count'] = 0

    if 'random_word' in request.session.keys():
        request.session['random_word'] = '0123456789ABCD'

    return redirect('/')