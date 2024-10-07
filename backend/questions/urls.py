from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('question/<slug:question_slug>/', views.question, name='question'),
]