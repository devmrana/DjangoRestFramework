from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
import json
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer

# Retrive all Students
def students(request):
    students = Student.objects.all()
    # print(students)
    serializer = StudentSerializers(students,many=True)
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data,safe=False) # By default safe=True , non-dict objects that's why need to safe=False for multiple value

# Students Details
def student_details(request,std_id):
    student = Student.objects.get(id=std_id)
    serializer = StudentSerializers(student)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)



# Deserialization insert Data
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Save'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res)
        # json_data =JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors)
