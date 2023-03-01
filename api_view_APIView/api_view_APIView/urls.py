from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # For Function Based @api_view url
    path('student-api_view/', views.StudentInfo, name='studentfbview'),
    path('student-api_view/<int:pk>/', views.StudentInfo, name='studentfbview'),
    
    # For Class Based APIView url
    path('student-APIView/', views.StudentInfoAPIView.as_view(), name='studentcbview'),
    path('student-APIView/<int:pk>/', views.StudentInfoAPIView.as_view(), name='studentcbview'),
]
