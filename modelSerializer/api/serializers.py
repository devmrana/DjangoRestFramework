from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Name should br start with 'R' ")
    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        # read_only_fields = ['name','city']
        # extra_kwargs = {
        #     'name':{'read_only':True}
        # }
    
    # Field Level Validation
    # def validate_roll(self,value):
    #     if value > 200:
    #         raise serializers.ValidationError('Seat Full')
    
    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rana' and ct.lower() != 'bogra':
            raise serializers.ValidationError('City Must Be Bogra')
        return data