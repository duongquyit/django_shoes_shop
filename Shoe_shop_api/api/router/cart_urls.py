from django.urls import path

from ..controller import cart_controller

urlpatterns = [
    path('<int:user_id>/cart-owner', cart_controller.getCartByUserId, name='cart-owner'),
    path('<int:id>/update-quantity', cart_controller.updateProductQuantity, name='update-product-quantity'),
    path('create-cart', cart_controller.createCart, name='create-cart'),
    path('<int:id>/delete', cart_controller.deleteCartById, name='delete-cart'),
]