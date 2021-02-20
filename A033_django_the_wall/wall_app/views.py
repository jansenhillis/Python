from django.shortcuts import render, redirect
from login_app.models import User
from wall_app.models import Message, Comment
from django.contrib import messages

def index(request):
    # check to see if the userid has been placed into the session
    if 'user_id' in request.session:
        user = User.objects.filter(id=request.session['user_id'])
        messages = Message.objects.all()

        return render(request, 'wall.html', {
            "auth_user": user[0],
            "messages": messages,
        })

def post_message(request):
    if request.method == "POST":
        errors = Message.objects.validator(request.POST)

        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/wall')
        else:
            # check to see if the userid has been placed into the session
            if 'user_id' in request.session:
                user = User.objects.filter(id=request.session['user_id'])
                if user:
                    message_text = request.POST['message']
                    message = Message.objects.create(user=user[0], message=message_text)
                    
                    return redirect('/wall')
                else: # user not found
                    messages.error(request, "User not found. Please login.")
                    return redirect('/')
            else:
                messages.error(request, "User not logged in.")
                return redirect('/')

def comment(request):
    if request.method == "POST":
        errors = Message.objects.validator(request.POST)

        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/wall')
        else:
            user = User.objects.filter(id=request.session['user_id'])
            message = Message.objects.filter(id=request.POST['message_id'])
            print(user, message)
            
            if user and message:
                comment_text = request.POST['comment']
                comment = Comment.objects.create(user=user[0], message=message[0], comment=comment_text)
                print(comment)
                return redirect('/wall')
            else:
                print("Error")
                messages.error(request, "User or Message not found.")
                return redirect('/wall')
