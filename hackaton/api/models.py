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
    duration = models.TextField(verbose_name='Длительность обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Кружок'
        verbose_name_plural = u'Кружки'


class Event(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.TextField(verbose_name='Название')
    status = models.TextField(verbose_name='Статус')
    price = models.TextField(verbose_name='Стоимость')
    type = models.TextField(verbose_name='Тип')
    direction = models.TextField(verbose_name='Направленность')
    start_date = models.TextField(verbose_name='Дата начала')
    start_time = models.TextField(verbose_name='Время начала')
    stop_date = models.TextField(verbose_name='Дата окончания')
    stop_time = models.TextField(verbose_name='Время окончания')
    online = models.BooleanField(verbose_name='Проводится онлайн')
    place = models.TextField(verbose_name='Место проведения')
    area = models.TextField(verbose_name='Район')
    health_limitations = models.BooleanField(verbose_name='Доступно для лиц с ОВЗ')
    censorship = models.TextField(verbose_name='Возрастной ценз')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Мероприятие'
        verbose_name_plural = u'Мероприятия'


class Book(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.TextField(verbose_name='Название')
    authior = models.TextField(verbose_name='Автор')
    sity = models.TextField(verbose_name='Город')
    publishing = models.TextField(verbose_name='Издательство')
    year = models.TextField(verbose_name='Год')
    description = models.TextField(verbose_name='Описание')
    censorship = models.TextField(verbose_name='Возрастной ценз')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'