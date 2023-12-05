from django import forms
from mailing.models import Client, Mailing, Text_Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class Text_MailingForm(StyleFormMixin):
    class Meta:
        model = Text_Mailing
        fields = ('subject', 'body', 'mailing',)


class ClientForm(StyleFormMixin):
    class Meta:
        model = Client
        fields = '__all__'