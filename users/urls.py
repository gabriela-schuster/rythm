from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login, name='login'),
]
