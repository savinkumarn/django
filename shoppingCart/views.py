from django.shortcuts import render
from .models import SCart
from random import randint
from .items import Items
from .forms import ItemForm
# Create your views here.


def generateWorkfile():
    return 'WORKFILE' + str(f'{randint(1, 99999):05}')


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
    context = {
        "workfile": generateWorkfile(),
        "cartQty": 0,
        "items": [],
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
            print(request.POST)
            workfile = request.POST.get('workfile')
            cartQty = int(request.POST.get('cartQty')) + 1
            items = request.POST.get('items')
            item_number = request.POST.get('item_number')
            item_quantity = request.POST.get('item_quantity')
            dummy_item = {}
            dummy_item["number"] = item_number
            dummy_item["quantity"] = item_quantity
            items_list = items.strip('][').split(', ')
            items_list.append(dummy_item)
            print(items_list)
            context = {
                "workfile": workfile,
                "cartQty": cartQty,
                "items": items_list,
                "itemForm": ItemForm(),
            }

    return render(request, 'sCart/addOrder.html', context)
