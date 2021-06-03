from django import forms
from django.forms import ModelForm
from .models import Brand ,Product

# class CreateBrandForm(forms.Form):
#       brand_name = forms.CharField()

class CreateModelForm(forms.ModelForm):
      class  Meta:
             model = Brand
             fields = ["brand_name"]
class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

