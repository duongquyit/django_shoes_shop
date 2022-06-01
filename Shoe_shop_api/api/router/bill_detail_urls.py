from django.urls import path

from ..controller import bill_detail_controller

urlpatterns = [
    path('list-bill-detail', bill_detail_controller.getAllBillDetails, name='list-bill-detail'),
    path('<int:id>', bill_detail_controller.getBillDetailById, name='bill_detail'),
    path('create-bill-detail', bill_detail_controller.createBillDetail, name='create-bill-detail'),
]