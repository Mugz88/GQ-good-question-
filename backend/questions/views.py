from django.shortcuts import render

from questions.models import Questions
from questions.utils import q_search

def catalog(request, category_slug=None):
    
    out_answer = request.GET.get('out_answer', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    
    if category_slug==None and not query:
        questions = Questions.objects.all()
    elif query:
        questions = q_search(query)
    else:
        questions = Questions.objects.filter(category__slug=category_slug)
    
    if out_answer:
        questions = questions.filter(out_answer=True)
    
    if order_by and order_by != "default":
        questions = questions.order_by(order_by)    
    
    context: dict = {
        'title': "Каталог",
        'content': "Содержание каталога",
        'questions': questions,
        'slug_url': category_slug
    }
    return render(request, 'questions/catalog.html', context)

def question(request, question_slug):
    question = Questions.objects.get(slug=question_slug)
    
    context: dict = {
        'title': question.title,
        'question': question
    }
    
    return render(request, 'questions/question.html', context=context)