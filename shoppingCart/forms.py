from django import forms


class ItemForm(forms.Form):
    item_number = forms.IntegerField(max_value=9999999)
    item_quantity = forms.IntegerField(max_value=9999)
