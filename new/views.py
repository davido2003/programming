from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import ProgrammingNewsApi
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics
from . seriallizers import ProgrammingNewsApiSerializer


# Create your views here.

class ProgrammingNewsApiView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProgrammingNewsApiSerializer
    queryset = ProgrammingNewsApi.objects.all()
    
    lookup_field = 'id'
    def get(self, request, id=None):         
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
   
    def delete(self, request, id):
        return self.destroy(request,id)