from random import randint
from .items import createItemObject
from .customer import create_customer
from .forms import ItemForm, CustomerForm, PaymentForm

# declaring global variables
cart = {}


def generateWorkfile():
    return 'WORKFILE' + str(f'{randint(1, 99999):05}')


def initialize_global_var():
    """
    This function needs to be called when
        > creating a new order
    """
    global cart
    cart["workfile"] = generateWorkfile()
    cart["cartQty"] = 0
    cart["items"] = []
    cart["customer"] = None
    pass


def get_global_cart():
    global cart
    return cart


def inc_global_cartQty():
    global cart
    cart["cartQty"] = cart["cartQty"] + 1
    pass


def addItem_global_itemsList(formData):
    global cart
    createItemObject(formData, cart["items"])
    pass


def addCustomer_cartData(formData):
    global cart
    cart["customer"] = create_customer(formData.get('customer_Id'))
    pass


def get_context_for_addOrder():
    context = {
        "cart": get_global_cart(),
        "itemForm": ItemForm(),
        "customerForm": CustomerForm(),
        "paymentView": False,
    }
    return context
