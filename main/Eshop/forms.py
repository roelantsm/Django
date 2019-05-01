from django import forms
from .models import Category
from .models import Product
from .models import Adress

class CategoryForm(forms.Form):
    soort = forms.CharField(max_length=200)
    # class Meta:
    #     model = category
    #     fields = [
    #         'soort']


class CategoryModelForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ('soort',)


class AdressForm(forms.ModelForm):
    class Meta: 
        model = Adress
        fields = ('straat',
        'nr', 
        'stad', 
        'postcode',
        'land')

class ProductModelForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ('naam',
        'category',
        'prijs',
        'btw',
        'merk',
        'korting',
        'image',
        'productCount')

class getQuantity(forms.Form):
    qty = forms.IntegerField()

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)