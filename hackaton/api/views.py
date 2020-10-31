from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

import api.models as models
import api.serializers as serializers


class OrganizationView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Organization.objects.all()
        return Response(serializers.OrganizationSerializers(queryset))