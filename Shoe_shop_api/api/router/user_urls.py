from django.urls import path
from .. import views

urlpatterns = [
    path('list-users', views.getAllUsers, name='list-users'),
    path('signup', views.createUser, name='signup'),
]