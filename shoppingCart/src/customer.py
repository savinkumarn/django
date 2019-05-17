

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


def create_customer(customerId):
    dummy_customer = {}
    dummy_customer["customerId"] = customerId
    dummy_customer["name"] = "dummy Name"
    dummy_customer["address"] = getAddress()
    dummy_customer["phone"] = getPhone()
    return dummy_customer
