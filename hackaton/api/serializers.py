from rest_framework import serializers
import api.models as models

from functools import lru_cache


@lru_cache(maxsize=1024)
def OrganizationSerializers(organizations):
    result = []
    for organization in organizations:
        result.append({
            'id': organization.id,
            'name': organization.name,
            'street': organization.street,
            'metro': organization.metro,
        })
    return result


@lru_cache(maxsize=1024)
def GroupSerializers(groups):
    result = []
    for group in groups:
        result.append({
            'id': group.id,
            'name': group.name,
            'street': group.street,
            'metro': group.metro,
        })
    return result