from django.shortcuts import render

from questions.models import Questions

def catalog(request, category_slug=None):
    if category_slug==None:
        questions = Questions.objects.all()
    else:
        questions = Questions.objects.filter(category__slug=category_slug)
    
    context: dict = {
        'title': "Каталог",
        'content': "Содержание каталога",
        'questions': questions,
    }
    return render(request, 'questions/catalog.html', context)

def question(request, question_slug):
    question = Questions.objects.get(slug=question_slug)
    
    context: dict = {
        'title': question.title,
        'question': question
    }
    
    return render(request, 'questions/question.html', context=context)