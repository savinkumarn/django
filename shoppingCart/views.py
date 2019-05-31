from django.shortcuts import render
from .src.items import addItemToCart
from .src.forms import ItemForm, CustomerForm, PaymentForm
from .src.shoppingCart import createShoppingCart
from .src.mongo import get_all
from .src.customer import add_cust_det_to_order
from .src.payment import savePaymentInfo
from .src.utils import validateInput, create_context_for_error
# Create your views here.


def base(request):
    """
    This view creates the landing page shoppingCart App
    """
    return render(request, 'sCart/index.html', context=None)


def getAllRecords(request):
    """
    This view creates the landing page for
    seeing all orders.
    """
    return render(request, 'sCart/allOrders.html', {"all_orders": get_all()})


def addOrder(request):
    """
    This view creates the landing page for
    creating a new order.
    """
    context = createShoppingCart()
    return render(request, 'sCart/addOrder.html', context)


def saveOrder(request):
    """
    This view validates the form data
    and calls the save customer function.
    """
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            context = add_cust_det_to_order(request.POST)
            return render(request, 'sCart/addOrder.html', context)


def completeSale(request):
    """
    This view validates the form data
    and calls the save payment function
    """
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            page, context = savePaymentInfo(request.POST)
            return render(request, page, context)


def addItem(request):
    """
    This view validates the form data
    and calls the item add function
    """
    # if request.method == 'POST':
    #     form = ItemForm(request.POST)
    #     if form.is_valid():
    #         context = addItemToCart(request.POST)
    #         return render(request, 'sCart/addOrder.html', context)
    if validateInput(request, 'POST', 'itemForm'):
        context = addItemToCart(request.POST)
        return render(request, 'sCart/addOrder.html', context)
    else:
        context = create_context_for_error(request,False,"Invalid Item Details")
        return render(request, 'sCart/addOrder.html', context={})
