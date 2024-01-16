from django import forms
from mailing.models import Client, Text_Mailing, Log_Mailing


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
        fields = ('client_email', 'client_fio', 'client_comment',)


class Log_MailingForm(StyleFormMixin):
    class Meta:
        model = Log_Mailing
        fields = ('datatime_last_attempt', 'status_attempt', 'answer_mail_server', 'mailing',)

