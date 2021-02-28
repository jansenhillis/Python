from django.shortcuts import render, redirect
from .models import Book
from login_app.models import User
from django.contrib import messages
from A034_django_favorite_books.decorators import authenticate_user

@authenticate_user
def index(request):
    auth_user = User.objects.get(pk=request.session['user_id'])
    books = Book.objects.all()
    
    return render(request, 'books.html', {
        "auth_user": auth_user,
        "books": books,
    })

@authenticate_user
def show_book(request, pk):
    auth_user = User.objects.get(pk=request.session['user_id'])
    book = Book.objects.filter(pk=pk)

    if book:
        return render(request, 'show.html', {
            "auth_user": auth_user,
            "book": book.first(),
        })
    else:
        return redirect('/books')

@authenticate_user
def add_favorite(request, pk):
    auth_user = User.objects.get(pk=request.session['user_id'])
    book = Book.objects.filter(pk=pk)

    if book:
        auth_user.books_favorited.add(book.first())

    messages.success(request, "This book has been added to your favorites.")
    return redirect(f'/books/{book.first().pk}')

@authenticate_user
def remove_favorite(request, pk):
    auth_user = User.objects.get(pk=request.session['user_id'])
    book = Book.objects.filter(pk=pk)
    
    if book:
        auth_user.books_favorited.remove(book.first())

    messages.success(request, "This book has been removed from your favorites.")
    return redirect(f'/books/{book.first().pk}')

@authenticate_user
def process_book(request):
    if request.method == "POST":
        auth_user = User.objects.get(pk=request.session['user_id'])
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

@authenticate_user
def update_book(request, pk):
    if request.method == "POST":
        auth_user = User.objects.get(pk=request.session['user_id'])
        book = Book.objects.get(pk=pk)
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

@authenticate_user
def delete_book(request, pk):
    if request.method == "POST":
        auth_user = User.objects.get(pk=request.session['user_id'])
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