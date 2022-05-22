from django.urls import path
from .. import views

urlpatterns = [
    path('list-categories', views.getListCategory, name='list-categories'),
    path('<int:id>', views.getCategoryById, name='category-detail'),
    path('<int:id>/product', views.getProductByCategoryId, name="product-by-category-id"),
]