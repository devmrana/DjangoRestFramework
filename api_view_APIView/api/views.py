from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# For Function Based @api_view
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def StudentInfo(request,pk=None):
  if request.method == 'GET':
      id = pk
      if id is not None:
          stu = Student.objects.get(pk=id)
          serializer = StudentSerializer(stu)
          return Response(serializer.data)
      stu = Student.objects.all()
      serializer = StudentSerializer(stu,many=True)
      return Response(serializer.data)

  if request.method == 'POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Created','data':request.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'PUT':
    # id = pk
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Update'})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'PATCH':
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu,data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Partial Update'})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'DELETE':
    student = Student.objects.get(id=pk)
    student.delete()
    return Response({'msg':'Data Deleted!!'})

# Class based APIView
from rest_framework.views import APIView
class StudentInfoAPIView(APIView):
  def get(self,request,format=None,pk=None):
    id = pk
    if id is not None:
      stu = Student.objects.get(id=id)
      serializer = StudentSerializer(stu)
      return Response(serializer.data)
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    return Response(serializer.data)

  def post(self,request,format=None):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  # PUT => full update
  def put(self,request,format=None,pk=None):
    # id = pk
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Update'})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  # patch partial
  def patch(self,request,format=None,pk=None):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu,data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Partial Update'})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,format=None,pk=None):
    id = pk
    student = Student.objects.get(id=id)
    student.delete()
    return Response({'msg':'Data Deleted!!'})

