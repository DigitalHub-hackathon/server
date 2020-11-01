from rest_framework import serializers
import api.models as models

from functools import lru_cache


@lru_cache(maxsize=1024)
def OrganizationSerializers(organizations):
    #f = open('api/org.csv', 'r')
    #for l in f.readlines():
    #    _, id_, name, street, metro = l.split(',')
    #    models.Organization(id=id_, name=name, street=street, metro=metro).save()
    #    print(name)
    #f.close()
    result = []
    for organization in organizations:
        result.append({
            'name': organization.name,
            'street': organization.street,
            'metro': organization.metro,
        })
    return result


@lru_cache(maxsize=1024)
def BookSerializers(books):
    result = []
    for book in books:
        result.append({
            'id': book.id,
            'name': book.name,
            'authior': book.authior,
            'sity': book.sity,
            'publishing': book.publishing,
            'year': book.year,
            'description': book.description,
            'censorship': book.censorship
        })
    return result


@lru_cache(maxsize=1024)
def GroupSerializers(groups):

    #f = open('api/k.csv', 'r')
    #for l in f.readlines():
    #    id_, finance, id_organization, schedule, name, duration = l.split('%')
    #    a = models.Organization.objects.filter(id=id_organization)
    #    if len(a):
    #        models.Group(id=id_, organization=a[0], name=name, finance=finance, schedule=schedule, duration=duration).save()
    #        print(name) 
    #f.close()

    result = []
    for group in groups:
        result.append({
            'id': group.id,
            'organization': {
                'name': group.organization.name,
                'street': group.organization.street,
                'metro': group.organization.metro,
            },
            'name': group.name,
            'finance': group.finance,
            'schedule': group.schedule,
            'duration': group.duration
        })
    return result


@lru_cache(maxsize=1024)
def EventSerializers(events):

    #f = open('api/Мероприятия.csv', 'r')
    #for l in f.readlines():
    #    id, name, status, price, type, direction, start_date, start_time, stop_date, stop_time, online, place, area, health_limitations, censorship =  l.split('%')
    #    models.Event(id=id, name=name, status=status, price=price, type=type, direction=direction, start_date=start_date, start_time=start_time, stop_date=stop_date, stop_time=stop_time, online=online, place=place, area=area, health_limitations=health_limitations, censorship=censorship).save()
    #    print(name) 
    #f.close()

    result = []
    for event in events:
        result.append({
            'id': event.id,
            'name': event.name,
            'status': event.status,
            'price': event.price,
            'type': event.type,
            'direction': event.direction,
            'start_date': event.start_date,
            'start_time': event.start_time,
            'stop_date': event.stop_date,
            'stop_time': event.stop_time,
            'online': event.online,
            'place': event.place,
            'area': event.area,
            'health_limitations': event.health_limitations,
            'censorship': event.censorship
        })
    return result