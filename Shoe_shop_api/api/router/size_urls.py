from django.urls import path
from ..controller import size_controller

urlpatterns = [
    path('list-size', size_controller.getListSize, name='list-size'),
    path('<int:id>', size_controller.getSizeDetail, name='size-detail'),
]