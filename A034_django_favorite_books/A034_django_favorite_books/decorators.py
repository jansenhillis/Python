from functools import wraps
from django.http import HttpResponse
from login_app.models import User

def authenticate_user(func):
    @wraps(func)
    def func_wrapper(request, *args, **kwargs):
        try:
            user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])
            print("Authentiated User: ", user.first, user.last)
        except Exception as ex:
            print("User not found exception", str(ex))

        if user:
            return func(request, *args, **kwargs)

        return HttpResponse('Unauthorized', status=401)
    return func_wrapper