from django.urls import path
from . import views

app_name = 'shoppingCart'

urlpatterns = [
    path('', views.base, name='index'),
    path('allOrders/', views.getAllRecords, name='allOrders'),
    path('addOrder/', views.addOrder, name='addOrder'),
    path('saveOrder/', views.saveOrder, name='saveOrder'),
    path('addItem/', views.addItem, name='addItem'),
    path('completeSale/', views.completeSale, name='completeSale'),
]
