from django.urls import path

from ..controller import cart_controller

urlpatterns = [
    path('<int:user_id>/cart-owner', cart_controller.getCartByUserId, name='cart-owner'),
    path('<int:id>/update-quantity', cart_controller.updateProductQuantity, name='update-product-quantity'),
]