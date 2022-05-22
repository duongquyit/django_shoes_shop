from django.urls import path

from api import views

urlpatterns = [
    path('list-bill', views.getListDetailBill, name='list-bill'),
    path('<int:id>', views.getDetailBill, name='bill-detail'),
]