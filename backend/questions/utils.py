from django.db.models import Q

from questions.models import Questions
def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Questions.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]
    
    q_objects = Q()
    
    for token in keywords:
        q_objects |= Q(title__icontains=token) | Q(text__icontains=token)
        
    return Questions.objects.filter(q_objects)