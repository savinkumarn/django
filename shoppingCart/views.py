from django.shortcuts import render
from .models import SCart
# Create your views here.


def base(request):
    return render(request, 'sCart/index.html',context=None)


def getAllRecords(request):
    all = SCart.objects.all()
    context = {
        "all_orders": all
    }
    return render(request, 'sCart/allOrders.html', context)


def addOrder(request):
    return render(request, 'sCart/index.html', context=None)
