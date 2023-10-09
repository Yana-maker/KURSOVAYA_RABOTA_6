from django import forms
from catalog.models import Product, Contacts, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        if 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар' in cleaned_data:
            raise forms.ValidationError('подобные продукты нельзя создавать')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        if 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар' in cleaned_data:
            raise forms.ValidationError('подобные слова нельзя вносить в описание')
        return cleaned_data


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if '@' not in cleaned_data:
            raise forms.ValidationError('почта должна содержать знак @')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
