from django.urls import path

from otvets import views

app_name = 'otvets'

urlpatterns = [
    path('otvet_add/<slug:question_slug>/', views.otvet_add, name='otvet_add'),
    path('otvet_change/<slug:question_slug>/<int:otvet_id>/', views.otvet_change, name='otvet_change'),
    path('otvet_delete/<int:otvet_id>/', views.otvet_delete, name='otvet_delete'),
]