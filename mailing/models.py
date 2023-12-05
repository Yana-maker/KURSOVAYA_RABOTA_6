from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Client(models.Model):
    client_email = models.EmailField(verbose_name='почта')
    client_fio = models.CharField(max_length=500, verbose_name='фио')
    client_comment = models.CharField(max_length=500, verbose_name='комментарий')

    def __str__(self):
        return f"{self.client_fio}"

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('client_fio',)

class Frequency:
    choises = (
        ("ежедневно", "daily"),
        ("еженедельно", "weekly"),
        ("ежемесячно", "monthly"),
    )


class Mailing(models.Model):
    name = models.CharField(verbose_name='название')
    time = models.DateTimeField(verbose_name='время и дата рассылки')
    frequency = models.CharField(max_length=11, choices=Frequency.choises, default='daily',verbose_name='периодичность')
    mailing_status = models.CharField(default='создана', choices=settings.STATUS, **NULLABLE, verbose_name='статус')
    client_email = models.ManyToManyField('Client', verbose_name='клиенты', **NULLABLE)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('frequency',)


class Text_Mailing(models.Model):
    subject = models.CharField(verbose_name='тема письма')
    body = models.CharField(verbose_name='тело письма')
    mailing = models.ForeignKey(Mailing, verbose_name='название', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.subject}"

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'
        ordering = ('subject',)

class Log_Mailing(models.Model):
    datatime_last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_attempt = models.CharField(default='НЕ УСПЕШНО', choices=settings.STATUS_ATTEMPT,
                                      verbose_name='статус попытки')
    answer_mail_server = models.TextField(**NULLABLE, verbose_name='ответ почтового сервера, если он был')
    mailing = models.ForeignKey(Mailing, verbose_name='название', on_delete=models.DO_NOTHING, **NULLABLE)

    def __str__(self):
        return f"{self.answer_mail_server}"

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'
        ordering = ('status_attempt',)
