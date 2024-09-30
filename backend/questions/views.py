from django.shortcuts import render


def catalog(request):
    return render(request, 'questions/catalog.html')

def question(request):
    return render(request, 'questions/question.html')