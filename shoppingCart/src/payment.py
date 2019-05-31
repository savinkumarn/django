from .utils import create_order_context
from .shoppingCart import getCart
from .mongo import save_payment_info, get_all


def deductMoney(cart):
    total = cart["cartTotal"]
    balance = total
    paidAmount = 0
    if len(cart["payments"]) > 0:
        for eachPayment in cart["payments"]:
            paidAmount += eachPayment["tenderAmount"]
        balance = total - paidAmount
    return balance


def get_payment_obj(formData):
    payment = {}
    payment["tenderAmount"] = float(formData.get('tenderAmount'))
    payment["tenderType"] = formData.get('tenderType')
    payment["tenderCardType"] = formData.get('cardType')
    return payment


def getContext(workfile):
    cart = getCart(workfile)
    total = cart["cartTotal"]
    balance = deductMoney(cart)
    context = {}
    if balance > 0:
        context = create_order_context(cart, True)
        context["balance"] = balance
        context["total"] = total
        page = 'sCart/addOrder.html'
    else:
        context = {"all_orders": get_all()}
        page = 'sCart/allOrders.html'
    return page, context


def savePaymentInfo(formData):
    workfile = formData.get('workfile')
    payment = get_payment_obj(formData)
    save_payment_info(workfile, payment)
    return getContext(workfile)
