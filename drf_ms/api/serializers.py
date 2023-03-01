# Works with nested serializers
from .models import Singer,Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields = '__all__'
        fields = ['id','title','duration','singer']

class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True,read_only=True) # sungby use model related_name, so here use it.
    class Meta:
        model = Singer
        fields = ['id','name','gender','sungby']
    
      


