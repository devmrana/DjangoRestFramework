from django.shortcuts import render
from . models import *
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def studentAPI(request):
    # Get request and view data
    if request.method == "GET":
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id',None)
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            else:
                stu = Student.objects.all()
                serializer = StudentSerializer(stu,many=True)
                # json_data = JSONRenderer().render(serializer.data)
                # return HttpResponse(json_data, content_type='application/json')
                return JsonResponse(serializer.data, safe=False)
        except Exception as m:
            response = JsonResponse({"msg":m.args})
            response.status_code = 500
            return response

    # Post request and save data
    elif request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        dataserializer = StudentSerializer(data=pythondata)
        if dataserializer.is_valid():
            dataserializer.save()
            res = {'msg':'Data Save'}
            return JsonResponse(res)
        res = {'msg':'Data not save'}
        return JsonResponse(res)

    # Update data
    elif request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        # dataserializer = StudentSerializer(stu,data=pythondata, partial=True) # Partial True all DATA not required!!!
        dataserializer = StudentSerializer(stu,data=pythondata) # All DATA required
        if dataserializer.is_valid():
            dataserializer.save()
            res = {'msg':'Data Updated'}
            return JsonResponse(res)
        json_data = JSONRenderer().render(dataserializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    # Delete data
    elif request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted'}
        return JsonResponse(res)
    


from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class StudentClassBasedAPI(View):
    def get(self,request, *args, **kwargs):
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id',None)
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            else:
                stu = Student.objects.all()
                serializer = StudentSerializer(stu,many=True)
                # json_data = JSONRenderer().render(serializer.data)
                # return HttpResponse(json_data, content_type='application/json')
                return JsonResponse(serializer.data, safe=False)
        except Exception as m:
            response = JsonResponse({"msg":m.args})
            response.status_code = 500
            return response
    def post(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        dataserializer = StudentSerializer(data=pythondata)
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
        dataserializer = StudentSerializer(stu,data=pythondata, partial=True) # Partial True all DATA not required!!!
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

from django.http import JsonResponse


# Work with Forntend JavaScript
# def ajax_get_view(request): # May include more arguments depending on URL parameters
#     # Get data from the database - Ex. Model.object.get(...)
#     # stu = Student.objects.all()
#     if request.method == "GET":
#         serializer = StudentSerializer(Student.objects.all(),many=True)
#         data  = serializer.data

#         return JsonResponse(data, safe=False)

@method_decorator(csrf_exempt,name='dispatch')
class ajax_get_view(View):
    def get(self,request, *args, **kwargs):
        serializer = StudentSerializer(Student.objects.all(),many=True)
        data  = serializer.data
        return JsonResponse(data, safe=False)
    
    def post(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        dataserializer = StudentSerializer(data=pythondata)
        if dataserializer.is_valid():
            dataserializer.save()
            res = {'msg':'Data Save'}
            return JsonResponse(res)
        res = {'msg':'Data not save..! Fields must be fillup'}
        return JsonResponse(res)


    