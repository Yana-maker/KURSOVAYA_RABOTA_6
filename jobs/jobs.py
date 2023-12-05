from config.settings import TIME_ZONE
import datetime
import pytz
from django.core.mail import send_mail
from mailing.models import Mailing, Log_Mailing, Client
from config.settings import EMAIL_HOST_USER

def send_mailings():
    current_time = datetime.datetime.now(pytz.timezone(TIME_ZONE))
    for mailing in Mailing.objects.filter(mailing_status='создана'):
        recepients = [client.client_email for client in mailing.client_email.all()]

        if mailing.frequency == 'daily' and current_time.hour == mailing.time.hour and current_time.minute == mailing.time.minute:
            message = mailing.message_set.all()
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=recepients,
            )


        elif mailing.frequency == 'weekly' and current_time.hour == mailing.time.hour and current_time.minute == mailing.time.minute and (current_time.day - mailing.time.day).days % 7 == 0:
            message = mailing.message_set.all()
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=recepients,
            )


        elif mailing.frequency == 'monthly' and current_time.hour == mailing.time.hour and current_time.minute == mailing.time.minute and (current_time.day - mailing.time.day).days % 30 == 0:
            message = mailing.message_set.all()
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=recepients,
            )

        Log_Mailing.objects.create(
            mailing=mailing,
            datatime_last_attempt=current_time,
            status_attempt='УСПЕШНО',
        )



