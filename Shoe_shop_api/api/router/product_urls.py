from django.urls import path
from .. import views

urlpatterns = [
    path('list-product', views.getListProduct, name='list-product'),
    path('<int:id>', views.getProductDetail, name='product-detail'),
    path('outstanding-product', views.getOutstandingProducts, name='outstanding-product'),
]