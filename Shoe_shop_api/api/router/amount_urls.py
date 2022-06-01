from django.urls import path
from ..controller import amount_controller

urlpatterns = [
    path('list-amount', amount_controller.getListAmounts, name='list-amount'),
    path('<int:id>', amount_controller.getAmountDetail, name='amount-detail'),
    path('<int:product_id>/<int:size_id>', amount_controller.getAmountByProductIdAndSizeId, name='amount-product-size'),
]