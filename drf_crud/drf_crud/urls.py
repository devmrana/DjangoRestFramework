"""drf_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views   # For Function Based
from api.views import StudentClassBasedAPI,ajax_get_view  # For Class Based
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.studentAPI),
    # path('students/',views.ajax_get_view), # es-6 ae fetch data url
    path('students/',ajax_get_view.as_view()),
    path('stdclsapi/', StudentClassBasedAPI.as_view()),

]

