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