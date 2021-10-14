from rest_framework import serializers
from . models import ProgrammingNewsApi
from django.db.models import fields 

class ProgrammingNewsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingNewsApi
        fields = [ 'id','title','link','video']
