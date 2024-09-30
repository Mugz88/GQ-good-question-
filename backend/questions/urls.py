from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('question/', views.question, name='question'),
]