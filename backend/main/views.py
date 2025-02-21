from django.shortcuts import render
from django.http import HttpResponse

from questions.models import Categories
from questions.models import Questions
def index(request):
    questions = Questions.objects.all().order_by('-date')
    context: dict ={   
        'title': "Главная",
        'content': "Вопросы на сайте",
        'questions': questions,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict ={   
        'title': "О сайте",
        'content': "Курсовая работа ",
        'text_on_page': "Выполнил: Натальин Александр ИВТ-13",
    }
    return render(request, 'main/about.html', context)