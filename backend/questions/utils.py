from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from questions.models import Questions
def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Questions.objects.filter(id=int(query))
    vector = SearchVector("title", "text")
    query = SearchQuery(query)

    return Questions.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

    # keywords = [word for word in query.split() if len(word) > 2]
    
    # q_objects = Q()
    
    # for token in keywords:
    #     q_objects |= Q(title__icontains=token) | Q(text__icontains=token)
        
    # return Questions.objects.filter(q_objects)