from django import template

from questions.models import Categories, Questions

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def user_questions(request):
    return Questions.objects.filter(author=request.user)