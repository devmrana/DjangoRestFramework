from django.urls import path
from . import views
urlpatterns = [
    path('', views.students, name='students'),
    path('student-details/<std_id>', views.student_details, name='student-details'),
    path('student-create/', views.student_create, name='student-create'),
]