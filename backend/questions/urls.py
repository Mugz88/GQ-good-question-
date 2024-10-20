from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('question_add/', views.question_add, name='question_add'),
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('question/<slug:question_slug>/', views.question, name='question'),
    path('question_delete/<int:question_id>/', views.question_delete, name='question_delete'),
]