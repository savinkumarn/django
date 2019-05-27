from django.shortcuts import render
from .src.items import addItemToCart
from .src.forms import ItemForm, CustomerForm, PaymentForm
from .src.shoppingCart import createShoppingCart, getCart
from .src.mongo import get_all
from .src.customer import add_cust_det_to_order
from .src.payment import savePaymentInfo
# Create your views here.


def base(request):
    return render(request, 'sCart/index.html', context=None)


def getAllRecords(request):
    return render(request, 'sCart/allOrders.html', {"all_orders": get_all()})


def addOrder(request):
    context = createShoppingCart()
    return render(request, 'sCart/addOrder.html', context)


def saveOrder(request):
    # context = get_context_for_addOrder()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            context = add_cust_det_to_order(request.POST)
            return render(request, 'sCart/addOrder.html', context)


def completeSale(request):
    # save the data
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            page, context = savePaymentInfo(request.POST)
    return render(request, page, context)


def addItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            context = addItemToCart(request.POST)
    return render(request, 'sCart/addOrder.html', context)
