from django.shortcuts import render
from .models import SCart
from .forms import ItemForm
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
    cart = initialize_global_var()
    context = {
        "cart": cart,
        "itemForm": ItemForm(),
    }
    return render(request, 'sCart/addOrder.html', context)


def saveOrder(request):
    context = None
    return render(request, 'sCart/addOrder.html', context)


def addItem(request):
    context = None
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            addItem_global_itemsList(request.POST)
            inc_global_cartQty()
            context = {
                "cart": get_global_cart(),
                "itemForm": ItemForm(),
            }
    return render(request, 'sCart/addOrder.html', context)
