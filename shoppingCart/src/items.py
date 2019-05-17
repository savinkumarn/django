from .price import Price, createPriceObject


class Items():
    def __init__(self):
        itemNumber = 0
        itemQuantity = 0
        itemVendorName = None
        itemModelNumber = None
        itemDescription = None
        itemPrice = Price()


def createItemObject(formData, items_list):
    dummy_item = {}
    dummy_item["number"] = formData.get('item_number')
    dummy_item["quantity"] = formData.get('item_quantity')
    dummy_item["vendorName"] = "vendorName"
    dummy_item["moderNumber"] = "modelNumber"
    dummy_item["description"] = "description bla bla"
    dummy_item["price"] = createPriceObject()
    items_list.append(dummy_item)
