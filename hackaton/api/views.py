from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

import api.models as models
import api.serializers as serializers

import api.predict as predict
import api.predict_events as predict_events
import api.predict_books as predict_books


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


class BookView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request, page):
        queryset = models.Book.objects.all()[page*100:(page+1)*100]
        return Response(serializers.BookSerializers(queryset))


class PredictGroupsView(viewsets.ViewSet):
    
    def all(self, request):
        ids = list(map(int, request.GET.get('likes').split(' ')))
        result = []
        for id in ids:
            index = predict.students[predict.students['id_услуги'] == id].index
            tmp = predict.cosine_sim[index]
            if not len(tmp):
                continue
            similar_movies = list(enumerate(tmp[0]))
            sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
            element = sorted_similar_movies[0]
            
            id_yslygi = int(predict.students.iloc[element[0]]['id_услуги'])
            group = models.Group.objects.filter(id=id_yslygi)

            s = serializers.GroupSerializers(group)[0]
            if s not in result:
                result.append(s)

        return Response(result)


class PredictBookssView(viewsets.ViewSet):
    
    def all(self, request):
        ids = list(map(int, request.GET.get('likes').split(' ')))
        result = []
        for id in ids:
            index = predict_books.books[predict_books.books['doc_id'] == id].index
            tmp = predict_books.cosine_sim[index]
            if not len(tmp):
                continue
            similar_movies = list(enumerate(tmp[0]))
            sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
            element = sorted_similar_movies[0]
            
            id_yslygi = int(predict_books.books.iloc[element[0]]['doc_id'])
            book = models.Book.objects.filter(id=id_yslygi)
            s = serializers.BookSerializers(book)[0]
            if s not in result:
                result.append(s)
                
        return Response(result)


class PredictEventView(viewsets.ViewSet):
    def all(self, request):
        ids = list(map(int, request.GET.get('likes').split(' ')))
        result = []
        for id in ids:
            index = predict_events.meropr[predict_events.meropr['id'] == id].index
            tmp = predict_events.cosine_sim[index]
            if not len(tmp):
                continue
            similar_movies = list(enumerate(tmp[0]))
            sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

            element = sorted_similar_movies[0]

            id_yslygi = int(predict_events.meropr.iloc[element[0]]['id'])
            event = models.Event.objects.filter(id=id_yslygi)

            s = serializers.EventSerializers(event)[0]
            if s not in result:
                result.append(s)

        return Response(result)