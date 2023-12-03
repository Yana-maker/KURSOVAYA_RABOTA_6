from django.contrib import admin

from mailing.models import Client, Mailing, Text_Mailing, Log_Mailing

# Register your models here.
admin.site.register(Client)
admin.site.register(Mailing)
admin.site.register(Text_Mailing)
admin.site.register(Log_Mailing)
