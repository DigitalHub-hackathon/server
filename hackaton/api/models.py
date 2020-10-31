from django.db import models


class Organization(models.Model):
    id = models.IntegerField(verbose_name='id')
    name = models.TextField(verbose_name='Название')
    streat = models.TextField(verbose_name='Улица')
    metro = models.TextField(verbose_name='Метро')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Организация'
        verbose_name_plural = u'Организации'


class Group(models.Model):
    id = models.IntegerField(verbose_name='id')
    name = models.TextField(verbose_name='Название')
    finance = models.TextField(verbose_name='Оплата')
    schedule = models.TextField(verbose_name='Расписание')
    duration = models.IntegerField(verbose_name='Длительность обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Кружок'
        verbose_name_plural = u'Кружки'