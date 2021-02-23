from django.shortcuts import render, redirect
from .models import Book
from login_app.models import User
from django.contrib import messages

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
            "book": book.first(),
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

    messages.success(request, "This book has been added to your favorites.")
    return redirect(f'/books/{book.first().pk}')

def remove_favorite(request, pk):
    auth_user = None if 'user_id' not in request.session else User.objects.get(pk=request.session['user_id'])
    if not auth_user:
        return redirect('/')

    book = Book.objects.filter(pk=pk)
    if book:
        auth_user.books_favorited.remove(book.first())

    messages.success(request, "This book has been removed from your favorites.")
    return redirect(f'/books/{book.first().pk}')

def process_book(request):
    if request.method == "POST":
        auth_user = None if 'user_id' not in request.session else User.objects.get(pk=request.session['user_id'])
        if not auth_user:
            return redirect('/')

        errors = Book.objects.validator(request.POST)
        if not errors:
            title = request.POST['title']
            desc = request.POST['desc']

            book = Book.objects.create(title=title, description=desc, uploaded_by_id=auth_user)
            book.favorited_by_id.add(auth_user)

            messages.success(request, f"Added {title} successfully!")
        else:
            for error in errors.values():
                messages.error(request, error)

    return redirect('/books')

def update_book(request, pk):
    if request.method == "POST":
        auth_user = None if 'user_id' not in request.session else User.objects.get(pk=request.session['user_id'])
        if not auth_user:
            return redirect('/')
        
        book = Book.objects.get(pk=pk)
        
        print(book)
        errors = Book.objects.validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
                return redirect(f'/books/{book.pk}')
        else:

            if book.uploaded_by_id == auth_user:
                book.title = request.POST['title']
                book.desc = request.POST['desc']
                book.save()
                messages.success(request, f"Updated {book.title} successfully!")
                return redirect(f'/books/{book.pk}')

def delete_book(request, pk):
    if request.method == "POST":
        auth_user = None if 'user_id' not in request.session else User.objects.get(pk=request.session['user_id'])
        if not auth_user:
            return redirect('/')

        errors = Book.objects.validator(request.POST)
        if not errors:
            book = Book.objects.filter(pk=pk)
            if book and book.first().uploaded_by_id == auth_user:
                book.first().delete()
                messages.success(request, "This book has been deleted.")
        else:
            for error in errors.values():
                messages.error(request, error)

    return redirect(f'/books')