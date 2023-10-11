from django import forms
from catalog.models import Product, Contacts, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class ProductForm(StyleFormMixin, forms.ModelForm):

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        name = self.cleaned_data['product_name'].lower()

        for word in self.forbidden_words:
            if word in name:
                raise forms.ValidationError(f"Нельзя использовать слово '{word}' в названии продукта.")
        return name

    def clean_product_description(self):
        name = self.cleaned_data['product_description'].lower()

        for word in self.forbidden_words:
            if word in name:
                raise forms.ValidationError(f"Нельзя использовать в описании слово '{word}' в названии продукта.")
        return name


class ContactsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if '@' not in cleaned_data:
            raise forms.ValidationError('почта должна содержать знак @')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
