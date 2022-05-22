from django.urls import path
from .. import views

urlpatterns = [
    path('list-size', views.getListSize, name='list-size'),
    path('<int:id>', views.getSizeDetail, name='size-detail'),
]