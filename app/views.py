from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from app.models import *
from django.http import HttpResponse
from datetime import date, timedelta


def book_list(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})


def add_books(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
            quantity=request.POST['quantity']
        )
        return redirect('book_list')
    return render(request, 'add_books.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.quantity = request.POST['quantity']
        book.save()
        return redirect('book_list')
    return render(request, 'edit_books.html', {'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    if Transaction.objects.filter(book=book, is_returned=False).exists():
        return HttpResponse("Cannot delete: this book is currently issued to someone.")
    book.delete()
    return redirect('book_list')


def issue_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        if book.quantity > 0:
            Transaction.objects.create(
                book=book,
                borrower_name=request.POST['borrower_name'],
                borrower_email=request.POST['borrower_email'],
                due_date=date.today() + timedelta(days=14)
            )
            book.quantity -= 1
            book.save()
            return redirect('transaction_list')
        else:
            return HttpResponse("No copies available")
    return render(request, 'issue_book.html', {'book': book})


def return_book(request, transaction_id):
    txn = Transaction.objects.get(id=transaction_id)
    txn.is_returned = True
    txn.return_date = date.today()

    if txn.return_date > txn.due_date:
        days_late = (txn.return_date - txn.due_date).days
        txn.fine_amount = days_late * 5

    txn.save()
    txn.book.quantity += 1
    txn.book.save()
    return redirect('transaction_list')


def transaction_list(request):
    transactions = Transaction.objects.filter(is_returned=False)
    return render(request, 'transaction_list.html', {
        'transactions': transactions,
        'today': date.today()
    })