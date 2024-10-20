from django import template

from questions.models import Questions
from otvets.models import Otvets

register = template.Library()

@register.simple_tag
def user_otvets(request):
    otvets = Otvets.objects.filter(user=request.user)
    questions = Questions.objects.filter(id__in=[otvet.question.id for otvet in otvets])
    return {'questions': questions, 'otvets': otvets}