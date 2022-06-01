from django.urls import path
from ..controller import product_controller

urlpatterns = [
    path('list-product', product_controller.getListProduct, name='list-product'),
    path('<int:id>', product_controller.getProductDetail, name='product-detail'),
    path('outstanding-product', product_controller.getOutstandingProducts, name='outstanding-product'),
    path('<int:id>/product-amount', product_controller.getAmountProduct, name='product-amount'),
]