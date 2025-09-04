from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text_head = 'Заголовок'
    text_body = 'Содержание блаблабла'
    context = {'text_head': text_head, 'text_body': text_body}

    return render(request, 'catalog/index.html', context)
