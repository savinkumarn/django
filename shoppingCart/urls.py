from django.urls import path
from . import views

app_name = 'shoppingCart'

urlpatterns = [
    path('', views.base, name='index'),
    path('allOrders/', views.getAllRecords, name='allOrders'),
    path('addOrder/', views.addOrder, name='addOrder'),
]