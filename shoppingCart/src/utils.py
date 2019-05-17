from random import randint
from .items import createItemObject

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
    return cart


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
