from django.urls import path
from ..controller import category_controller

urlpatterns = [
    path('list-categories', category_controller.getListCategory, name='list-categories'),
    path('<int:id>', category_controller.getCategoryById, name='category-detail'),
    path('<int:id>/product', category_controller.getProductByCategoryId, name="product-by-category-id"),
]