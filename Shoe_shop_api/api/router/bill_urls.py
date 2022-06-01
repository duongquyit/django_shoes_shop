from django.urls import path

from ..controller import bill_controller

urlpatterns = [
    path('list-bill', bill_controller.getListDetailBill, name='list-bill'),
    path('<int:id>', bill_controller.getBillById, name='bill-detail'),
    path('create-bill', bill_controller.createBill, name='create-bill'),
]