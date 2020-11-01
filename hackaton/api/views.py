from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

import api.models as models
import api.serializers as serializers
import api.predict as predict


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
    
    def all(self, request):
        ids = list(map(int, request.GET.get('likes').split(' ')))
        result = []
        for id in ids:
            index = predict.students[predict.students['id_услуги'] == id].index
            similar_movies = list(enumerate(predict.cosine_sim[index][0]))
            sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
            element = sorted_similar_movies[0]
            print(element)
            id_yslygi = int(predict.students.iloc[element[0]]['id_услуги'])
            group = models.Group.objects.filter(id=id_yslygi)
            result += serializers.GroupSerializers(group)

        return Response(result)