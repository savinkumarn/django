
from djongo import models

# Create your models here.


class SCart(models.Model):
    workfile = models.CharField(max_length=100)
    cartQty = models.IntegerField()
    customer = models.ManyToManyField('Customer')
    items = models.ArrayModelField(models.ManyToManyField('Items'))
    payments = models.ArrayModelField(models.ManyToManyField('Payment'))


class Customer(models.Model):
    customerID = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.ArrayModelField(models.ManyToManyField('Address'))
    phone = models.ManyToManyField('Phone')


class Address(models.Model):
    addressLine1 = models.CharField(max_length=100)
    addressLine2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Phone(models.Model):
    mobile = models.CharField(max_length=100)
    business = models.CharField(max_length=100)


class Items(models.Model):
    itemNumber = models.IntegerField()
    vendorName = models.CharField(max_length=100)
    modelNumber = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.ManyToManyField('Price')


class Price(models.Model):
    unitPrice = models.CharField(max_length=100)
    sellingPrice = models.CharField(max_length=100)
    unlockPrice = models.CharField(max_length=100)


class Payment(models.Model):
    tenderType = models.CharField(max_length=100)
    tenderAmount = models.CharField(max_length=100)
    cardType = models.CharField(max_length=100)
    cardInfo = models.ManyToManyField('CardInfo')


class CardInfo(models.Model):
    cardInfo_1 = models.CharField(max_length=100)
    cardInfo_2 = models.CharField(max_length=100)


class Entry(models.Model):
    sCart = models.EmbeddedModelField(
        model_container=SCart,
    )
    headline = models.CharField(max_length=255)
