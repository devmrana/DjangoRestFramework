from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField()
    roll = serializers.IntegerField()
    city = serializers.CharField()

    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')

    def create(self, validated_data):
        return Student.objects.create(**validated_data)   #all fields post data validation check

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        return instance