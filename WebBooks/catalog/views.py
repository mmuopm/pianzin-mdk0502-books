from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, BookInstance


def index(request):
    text_head = 'У нас большой выбор книг, у Литрес меньше'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status_exact=2).count()
    text_body = 'Содержание блаблабла'
    context = {'text_head': text_head, 'text_body': text_body}

    return render(request, 'catalog/index.html', context)
