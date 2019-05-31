from .mongo import get_all, getCartDetails
from .forms import ItemForm, CustomerForm, PaymentForm

forms = {
    'customerForm': CustomerForm,
    'itemForm': ItemForm,
    'paymentForm': PaymentForm,
}

views = {
    "paymentView": {
        "cart": "shoppingCart",
        "paymentView": True,
        "paymentForm": PaymentForm(),
    },
    "itemView": {
        "cart": "shoppingCart",
        "paymentView": False,
        "itemForm": ItemForm(initial={'item_quantity': 1}),
        "customerForm": CustomerForm(),
    }
}


def create_order_context(shoppingCart, paymentView):
    """
    shopping cart has the cart details,
    paymentView would we set to True if we have
    completed item and customer addition
    """
    if paymentView:
        context = views['paymentView']
    else:
        context = views['itemView']
    context["cart"] = shoppingCart
    return context


def create_context_for_error(request, paymentView, error_message):
    workfile = request.POST.get('workfile')
    cart = getCartDetails(workfile)
    context = create_order_context(cart, paymentView)
    context["errorMessage"] = error_message
    return context


def validateInput(request, requestType, formToValidate):
    if request.method == 'POST':
        form = forms[formToValidate](request.POST)
        if form.is_valid():
            return True
        else:
            return False
    else:
        return False
