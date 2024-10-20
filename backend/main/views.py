from django.shortcuts import render
from django.http import HttpResponse

from questions.models import Categories
from questions.models import Questions
def index(request):
    questions = Questions.objects.all().order_by('-date')
    context: dict ={   
        'title': "Главная",
        'content': "Содержание главной страницы",
        'questions': questions,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict ={   
        'title': "О сайте",
        'content': "Описание сайта",
        'text_on_page': "Текст на странице",
    }
    return render(request, 'main/about.html', context)