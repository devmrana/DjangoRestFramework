from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    stdclass = serializers.IntegerField()
    roll = serializers.IntegerField()
    city = serializers.CharField()

    # def validate_stdclass(self,value):
    #     if value >12:
    #         raise serializers.ValidationError('Only class-5 to class-11 available..!')
    # def validate_roll(self,value):
    #     if value >=200:
    #         raise serializers.ValidationError('Seat Full')

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(f'Old name ==> {instance.name}')
        instance.name = validated_data.get('name',instance.name)
        print(f'New name ==> {instance.name}')
        instance.stdclass = validated_data.get('stdclass',instance.stdclass)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

    


