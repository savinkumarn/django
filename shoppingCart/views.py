from django.shortcuts import render
from .models import SCart
# Create your views here.


def base(request):
    return render(request, 'sCart/index.html',context=None)


def getAllRecords(request):
    all = SCart.objects.using('scart_db').all()
    print(all)
    context = {
        "all_orders": all
    }
    return render(request, 'sCart/allOrders.html', context)


def addOrder(request):
    #my_object.save(using='scart_db')
    return render(request, 'sCart/addOrder.html', context=None)
