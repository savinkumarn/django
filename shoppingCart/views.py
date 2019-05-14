from django.shortcuts import render
from .models import SCart
from random import randint
from .items import Items
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
    }
    return render(request, 'sCart/addOrder.html', context)


def saveOrder(request):
    pass


def addItem(request):
    print(request.POST)
    context = {
        "workfile": generateWorkfile(),
        "cartQty": 0,
    }
    return render(request, 'sCart/addOrder.html', context)
