from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

import api.models as models
import api.serializers as serializers
import pandas as pd

from joblib import load

class OrganizationView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Organization.objects.all()
        return Response(serializers.OrganizationSerializers(queryset))


class GroupView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request, page):
        queryset = models.Group.objects.all()[page*100:(page+1)*100]
        return Response(serializers.GroupSerializers(queryset))


class EventView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request, page):
        queryset = models.Event.objects.all()[page*100:(page+1)*100]
        return Response(serializers.EventSerializers(queryset))


class PredictGroupsView(viewsets.ViewSet):
    #clf_rf = load('api/weight_groups.csv')
    #y = pd.read_csv(f'api/answer.csv')

    def all(self, request):
        return Response({"1": 1})