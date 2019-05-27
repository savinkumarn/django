from .price import createPriceObject
from .forms import ItemForm
from .utils import create_order_context
from .shoppingCart import getCart
from .mongo import add_item


def createItemObject(formData):
    dummy_item = {}
    dummy_item["itemNumber"] = formData.get('item_number')
    dummy_item["quantity"] = formData.get('item_quantity')
    dummy_item["vendorName"] = "vendorName"
    dummy_item["modelNumber"] = "modelNumber"
    dummy_item["description"] = "description bla bla"
    dummy_item["price"] = createPriceObject()
    dummy_item["totalValue"] = int(dummy_item["quantity"]) * dummy_item["price"]["sellingPrice"]
    return dummy_item


def addItemToCart(formData):
    item = createItemObject(formData)
    workfile = formData.get('workfile')
    add_item(item, workfile)
    cart = getCart(workfile)
    return create_order_context(cart, False)
