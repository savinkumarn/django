from django import forms

PAYMENT_CHOICES = (
    ("cash", "cash"),
    ("card", "card"),
    ("cheque", "cheque"))


class ItemForm(forms.Form):
    item_number = forms.IntegerField(max_value=9999999)
    item_quantity = forms.IntegerField(max_value=9999)


class CustomerForm(forms.Form):
    customer_Id = forms.CharField(max_length=10)


class PaymentForm(forms.Form):
    tenderType = forms.ChoiceField(choices=PAYMENT_CHOICES)
    tenderAmount = forms.CharField(max_length=100)
    cardType = forms.CharField(max_length=100)
