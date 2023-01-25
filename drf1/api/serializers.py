from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField()
    roll = serializers.IntegerField()
    city = serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
