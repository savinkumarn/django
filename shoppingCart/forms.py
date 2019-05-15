from django import forms


class ItemForm(forms.Form):
    item_number = forms.IntegerField()
    item_quantity = forms.IntegerField()
