from pymongo import MongoClient

#client = MongoClient("mongodb+srv://admin:admin@cluster0-4km6c.mongodb.net/test?retryWrites=true")
client = MongoClient("172.17.0.1:27017")
db = client.shoppingCart
orders = db.orders


def get_all():
    return orders.find()


def save_order(cart):
    orders.insert_one(cart)
    pass


def update_cart_qty(workfile, quantity):
    find_query = {
        "cart.workfile": workfile,
    }
    updateQuery = {
        "$inc": {
            "cart.cartQty": int(quantity)
        }
    }
    orders.update_one(find_query, updateQuery)
    pass


def update_cart_total(workfile, totalValue):
    find_query = {
        "cart.workfile": workfile,
    }
    updateQuery = {
        "$inc": {
            "cart.cartTotal": totalValue
        }
    }
    orders.update_one(find_query, updateQuery)
    pass


def add_item(item, workfile):
    find_query = {
        "cart.workfile": workfile,
    }
    updateQuery = {
        "$push": {
            "cart.items": item
        }
    }
    orders.update_one(find_query, updateQuery)
    # Now Update Cart Qty
    update_cart_qty(workfile, item["quantity"])
    update_cart_total(workfile, item["totalValue"])
    pass


def getCartDetails(workfile):
    rec = orders.find_one({"cart.workfile": workfile})
    return rec["cart"]


def save_cust_details(workfile, customer):
    find_query = {
        "cart.workfile": workfile,
    }
    updateQuery = {
        "$set": {
            "cart.customer": customer
        }
    }
    orders.update_one(find_query, updateQuery)
    pass


def save_payment_info(workfile, paymentDetails):
    find_query = {
        "cart.workfile": workfile,
    }
    updateQuery = {
        "$push": {
            "cart.payments": paymentDetails
        }
    }
    orders.update_one(find_query, updateQuery)
    pass
