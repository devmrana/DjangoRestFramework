from .models import Singer,Song
import json
from .serializers import SingerSerializer,SongSerializer
from rest_framework import viewsets
from django_filters import filters

# Retrive all Singer
class SingerViewSet(viewsets.ModelViewSet):    #viewsets.ModelViewSet ==> get & post data
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


# Retrive all Song
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    

