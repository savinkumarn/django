from .mongo import save_order, getCartDetails
from random import randint
from .utils import create_order_context


def createShoppingCart():
    shoppingcart = {
        "workfile": generateWorkfile(),
        "cartQty": 0,
        "cartTotal": 0.00,
        "items": [],
        "customer": "",
        "payments": [],
    }
    save_order({"cart": shoppingcart})
    return create_order_context(shoppingcart, False)


def generateWorkfile():
    return 'WORKFILE' + str(f'{randint(1, 99999):05}')


def getCart(workfile):
    return getCartDetails(workfile)
