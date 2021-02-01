from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime, timezone
    
def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "time2" : datetime.now(timezone.utc),
    }
    return render(request,'index.html', context)