from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # below syntax called list comprehension : short hand of a for loop that adds items to a list
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        # iterate through the rest of the fields and set classes
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'