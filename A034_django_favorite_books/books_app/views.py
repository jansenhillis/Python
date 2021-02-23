from django.shortcuts import render, redirect
from .models import Book
from login_app.models import User

def index(request):
    auth_user = None if 'user_id' not in request.session else User.objects.get(pk=request.session['user_id'])
    if not auth_user:
        return redirect('/')

    books = Book.objects.all()
    return render(request, 'books.html', {
        "auth_user": auth_user,
        "books": books,
    })

def show_book(request, pk):
    auth_user = None if 'user_id' not in request.session else User.objects.get(pk=request.session['user_id'])
    if not auth_user:
        return redirect('/')

    book = Book.objects.filter(pk=pk)
    if book:
        return render(request, 'show.html', {
            "auth_user": auth_user,
            "book": book[0],
        })
    else:
        return redirect('/books')

def add_favorite(request, pk):
    auth_user = None if 'user_id' not in request.session else User.objects.get(pk=request.session['user_id'])
    if not auth_user:
        return redirect('/')

    book = Book.objects.filter(pk=pk)
    if book:
        auth_user.books_favorited.add(book.first())

    return redirect('/books')
