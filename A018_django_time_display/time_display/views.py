from django.shortcuts import render
from time import gmtime, strftime
    
def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)