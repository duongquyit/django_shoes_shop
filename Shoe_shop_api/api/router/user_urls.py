from django.urls import path
from ..controller import user_controller

urlpatterns = [
    path('list-users', user_controller.getAllUsers, name='list-users'),
    path('signup', user_controller.createUser, name='signup'),
    path('signin', user_controller.signIn, name='signin'),
    path('<int:id>', user_controller.getUserById, name='get-user-informations'),
]