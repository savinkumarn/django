from django import forms

PAYMENT_CHOICES = (
    ("cash", "CASH"),
    ("card", "CARD"),
    ("cheque", "CHEQUE"))


class ItemForm(forms.Form):
    item_number = forms.IntegerField(max_value=9999999, label='Item Number')
    item_quantity = forms.IntegerField(max_value=9999, label='Item Qty')


class CustomerForm(forms.Form):
    customer_Id = forms.CharField(max_length=10, label='Customer ID')


class PaymentForm(forms.Form):
    tenderType = forms.ChoiceField(choices=PAYMENT_CHOICES, label='Tender Type')
    tenderAmount = forms.CharField(max_length=100, label='Tender Amount')
    cardType = forms.CharField(max_length=100, label='Card Type')
