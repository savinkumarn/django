from .utils import create_order_context
from .shoppingCart import getCart
from .mongo import save_cust_details
from copy import deepcopy


def getAddress():
    addressList = []
    for i in range(2):
        addDict = {}
        addDict["addressLine1"] = "3523423"
        addDict["addressLine2"] = "23453246"
        addDict["city"] = "3426"
        addDict["state"] = "sdfgsdf"
        addDict["zipCode"] = "214512"
        addDict["country"] = "IBDAIO"
        addressList.append(addDict)
    return addressList


def getPhone():
    dummy_phone = {}
    dummy_phone["mobile"] = "23463426"
    dummy_phone["business"] = "324632464236"
    return dummy_phone


def add_cust_det_to_order(formData):
    customer = {}
    customer["cust_id"] = formData.get("customer_Id")
    customer["name"] = "Customer Name"
    customer["address"] = getAddress()
    customer["phone"] = getPhone()
    workfile = formData.get('workfile')
    save_cust_details(workfile, customer)
    cart = getCart(workfile)
    total = float(cart["cartTotal"])
    balance = deepcopy(total)
    context = create_order_context(cart, True)
    context["total"] = total
    context["balance"] = balance
    return context
