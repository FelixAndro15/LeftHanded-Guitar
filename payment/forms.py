from django import forms
from . models import ShippingAddress
class ShippingForm(forms.ModelForm):
    class Meta:
        model=ShippingAddress
        fields = ['full_name', 'email', 'address1', 'address2', 'city', 'state', 'zipcode']
        exclude = ['user',]
        labels = {
            'full_name': 'Tam Ad',
            'email': 'Email',
            'address1': 'Adres 1',
            'address2': 'Adres 2',
            'city': 'Şehir',
            'state': 'Eyalet',
            'zipcode': 'Posta Kodu'
        }