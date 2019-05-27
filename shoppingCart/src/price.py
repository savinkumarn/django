from random import randint


def createPriceObject():
    dummy_item = {}
    price = round(randint(1, 9999) / 100.00, 2)
    dummy_item["unitPrice"] = price
    dummy_item["sellingPrice"] = price + 10.00
    dummy_item["unlockPrice"] = 0.00
    return dummy_item
