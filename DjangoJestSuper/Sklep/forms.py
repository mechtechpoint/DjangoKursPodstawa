from django import forms
from .models import Produkt, Koszyk

# class KoszykForm(forms.ModelForm):
#
#     class Meta:
#         model = Produkt
#         fields = ['dodane']
#         labels = {'dodane':''}


class KoszykForm(forms.ModelForm):

    class Meta:
        model = Koszyk
        fields = ['dodane_user']
        labels = {'dodane_user':''}

