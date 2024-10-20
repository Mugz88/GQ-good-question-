from django.shortcuts import render, redirect

from questions.models import Questions, Categories
from questions.utils import q_search
from otvets.models import Otvets

from django.contrib.auth.decorators import login_required 
from django.utils.text import slugify
from unidecode import unidecode

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
    answers = Otvets.objects.filter(question=question)

    context: dict = {
        'title': question.title,
        'question': question,
        'otvets': answers
    }

    return render(request, 'questions/question.html', context=context)

@login_required
def question_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        category_id = request.POST.get('category')
        if title and text and category_id:
            category = Categories.objects.get(id=category_id)
            slug = slugify(unidecode(title))
            Questions.objects.create(title=title, text=text, category=category, author=request.user, slug=slug)
        else:
            pass
        return redirect(request.META['HTTP_REFERER'])