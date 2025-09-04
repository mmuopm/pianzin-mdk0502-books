from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, BookInstance, Author


def index(request):
    text_head = 'У нас большой выбор книг, у Литрес меньше'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status_exact=2).count()

    author = Author.objects
    num_author = Author.objects.count()
    context = {'text_head' : text_head,
               'books': books, 'num_books': num_books,
               'num_instance': num_instance,
               'num_instance_available' : num_instance_available,
               'author': author, 'num_author': num_author}

    text_body = 'Содержание блаблабла'
    context = {'text_head': text_head, 'text_body': text_body}

    return render(request, 'catalog/index.html', context)
