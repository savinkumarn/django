from random import randint


def getPrice(itemNumber):
    """
    dummy function to generate dummy item prices
    """
    price = 0
    if itemNumber < 999:
        price = round(itemNumber * 3.14, 2)
    elif itemNumber < 9999:
        price = round(itemNumber / 43, 2)
    elif itemNumber < 49999:
        price = round(itemNumber / 73, 2)
    elif itemNumber < 99999:
        price = round((itemNumber * 45) / 19911, 2)
    elif itemNumber < 499999:
        price = round((itemNumber * 34) / 33663, 2)
    elif itemNumber < 999999:
        price = round((itemNumber * 643) / 641521, 2)
    else:
        price = round((itemNumber * 3.14) / 987312, 2)
    return price


def createPriceObject(itemNumber):
    """
    dummy function to generate dummy item numbers
    """
    dummy_item = {}
    price = getPrice(int(itemNumber))
    dummy_item["unitPrice"] = price
    dummy_item["sellingPrice"] = price + 10.00
    dummy_item["unlockPrice"] = 0.00
    return dummy_item
