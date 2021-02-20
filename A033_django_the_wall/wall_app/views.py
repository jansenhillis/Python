from django.shortcuts import render
from login_app.models import User

def index(request):
    # check to see if the userid has been placed into the session
    if 'user_id' in request.session:
        user = User.objects.filter(id=request.session['user_id'])

    return render(request, 'wall.html', {
        "user": user[0]
    })