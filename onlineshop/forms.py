from django import forms
from django.forms import fields
from onlineshop.models import Product, Brand, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'photo', 'brand')

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )