from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-otvets/', views.users_otvets, name='users_otvets'),
    path('logout/', views.logout, name='logout'),
]