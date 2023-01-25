from django.shortcuts import render
from . models import Student
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
# Retrive all Students


@method_decorator(csrf_exempt,name='dispatch')
class StudentClassBasedAPI(View):
    def get(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = str(JSONParser().parse(stream))
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        else:
            stu = Student.objects.all()
            serializer = StudentSerializers(stu,many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
            # return JsonResponse(serializer.data, safe=False)
    
    def post(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        dataserializer = StudentSerializers(data=pythondata)
        if dataserializer.is_valid():
            dataserializer.save()
            res = {'msg':'Data Save'}
            return JsonResponse(res)
        res = {'msg':'Data not save'}
        return JsonResponse(res)

    def put(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        dataserializer = StudentSerializers(stu,data=pythondata, partial=True) # Partial True all DATA not required!!!
        # dataserializer = StudentSerializer(stu,data=pythondata) # All DATA required
        if dataserializer.is_valid():
            dataserializer.save()
            res = {'msg':'Data Updated'}
            return JsonResponse(res)
        json_data = JSONRenderer().render(dataserializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted'}
        return JsonResponse(res,safe=False)