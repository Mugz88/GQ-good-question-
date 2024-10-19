from django.shortcuts import render, redirect

from questions.models import Questions
from otvets.models import Otvets

def otvet_add(request, question_slug):
    if request.method == 'POST':
        discription = request.POST.get('discription')
        question = Questions.objects.get(slug=question_slug)
        if request.user.is_authenticated:
            Otvets.objects.create(user=request.user, question=question, discription=discription)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])

def otvet_change(request, otvet_id, question_slug):
    ''''''
def otvet_delete(request, otvet_id, question_slug):
    ''''''