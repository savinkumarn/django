from django.shortcuts import render
from .models import SCart
from .src.items import Items, createItemObject
from .forms import ItemForm
from .src.utils import generateWorkfile, initialize_global_var
# Create your views here.

# declaring global variables
workfile = None
qty = 0
items_list = []


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
    workfile, qty, items_list = initialize_global_var()
    context = {
        "workfile": workfile,
        "cartQty": qty,
        "items": items_list,
        "itemForm": ItemForm(),
    }
    return render(request, 'sCart/addOrder.html', context)


def saveOrder(request):
    pass


def addItem(request):
    context = None
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            createItemObject(request.POST, items_list)
            qty = len(items_list)
            context = {
                "workfile": workfile,
                "cartQty": qty,
                "items": items_list,
                "itemForm": ItemForm(),
            }

    return render(request, 'sCart/addOrder.html', context)
