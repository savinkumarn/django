from django.shortcuts import render
from .models import SCart
from .src.utils import *
# Create your views here.


def base(request):
    return render(request, 'sCart/index.html', context=None)


def getAllRecords(request):
    all = SCart.objects.using('scart_db').all()
    print(all)
    context = {
        "all_orders": all
    }
    return render(request, 'sCart/allOrders.html', context)


def addOrder(request):
    initialize_global_var()
    context = get_context_for_addOrder()
    return render(request, 'sCart/addOrder.html', context)


def saveOrder(request):
    context = get_context_for_addOrder()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            addCustomer_cartData(request.POST)
            context["paymentView"] = True
            context["paymentForm"] = PaymentForm()
    return render(request, 'sCart/addOrder.html', context)


def completeSale(request):
    pass


def addItem(request):
    context = get_context_for_addOrder()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            addItem_global_itemsList(request.POST)
            inc_global_cartQty()
            context["cart"] = get_global_cart()
    return render(request, 'sCart/addOrder.html', context)
