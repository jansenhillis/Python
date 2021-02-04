from django.shortcuts import render, redirect
import random
from datetime import datetime

forms = {
    'farm': { 'min': 10, 'max': 20 },
    'cave': { 'min': 5, 'max': 10 },
    'house': { 'min': 2, 'max': 5 },
    'casino': { 'min': -50, 'max': 50 },
}

def index(request):
    if 'owned_gold' not in request.session.keys():
        request.session['owned_gold'] = 0
        request.session['activities'] = {}
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'POST':
        
        # min/max values for each form
        if 'farm' in request.POST:
            values = forms['farm']
            form = 'farm'
        elif 'cave' in request.POST:
            values = forms['cave']
            form = 'cave'
        elif 'house' in request.POST:
            values = forms['house']
            form = 'house'
        elif 'casino' in request.POST:
            values = forms['casino']
            form = 'casino'

        delta = get_random_number_between(values['min'], values['max'])
        request.session['owned_gold'] += delta
        request.session['activities'][str(datetime.now())] = get_log_entry(delta, form)

        return redirect('/')
    else:
        return redirect('/')

# impl of randInt(<min>, <max>) using random (from A007-python-functionsIntermediate2)
# Modulus sets the upper bound, late addition of min sets the lower bound
# (max + 1) to make sure the maximum value is included in the result inclusively
def get_random_number_between(min=0, max=100):
    
    # basic type checking
    if not isinstance(min, int):
        return "minimum is not an integer"
    elif not isinstance(max, int):
        return "maximum is not an integer"

    # basic range check
    if (min > max):
        return "minimum cannot be larger than maximum"

    num = (round(random.random() * 100) % ((max + 1) - min)) + min
    return num


def get_log_entry(delta, form):
    if delta > 0:
        string = "Earned $" + str(delta) + " gold from the " + form + "!"
    else:
        string = "Entered a casino and lost " + str(abs(delta)) + " gold!"

    return string
