from django.urls import path
from .. import views

urlpatterns = [
    path('list-amount', views.getListAmounts, name='list-amount'),
    path('<int:id>', views.getAmountDetail, name='amount-detail'),
]