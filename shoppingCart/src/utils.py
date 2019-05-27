from .mongo import get_all, add_item
from .forms import ItemForm, CustomerForm, PaymentForm


def create_order_context(shoppingCart, paymentView):
    """
    shopping cart has the cart details,
    paymentView would we set to True if we have
    completed item and customer addition
    """
    context = {
        "cart": shoppingCart,
        "paymentView": paymentView,
        "itemForm": ItemForm(),
        "customerForm": CustomerForm(),
        "paymentForm": PaymentForm(),
    }
    return context
