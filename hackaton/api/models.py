from django.db import models


class Organization(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.TextField(verbose_name='Название')
    street = models.TextField(verbose_name='Улица')
    metro = models.TextField(verbose_name='Метро')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Организация'
        verbose_name_plural = u'Организации'


class Group(models.Model):
    PRICE = (
        (0, 'Бесплатно'),
        (1, 'Платно'),
    )

    TYPE_SCHEDULE = (
        (0, 'Общее'),
        (1, 'Индивидуальное')
    )

    id = models.IntegerField(verbose_name='id', primary_key=True)
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    name = models.TextField(verbose_name='Название')
    finance = models.IntegerField(choices=PRICE, verbose_name='Оплата')
    schedule = models.IntegerField(choices=TYPE_SCHEDULE, verbose_name='Расписание')
    duration = models.IntegerField(verbose_name='Длительность обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Кружок'
        verbose_name_plural = u'Кружки'