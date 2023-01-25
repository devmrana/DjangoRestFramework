from django.contrib import admin
from django.urls import path,include
# from api import views
from api.views import StudentClassBasedAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentClassBasedAPI.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
