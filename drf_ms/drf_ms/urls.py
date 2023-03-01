from django.contrib import admin

from django.urls import path, include


# import rest_framework
from rest_framework.routers import DefaultRouter
route = DefaultRouter()
from api import views
route.register('singer',views.SingerViewSet, basename='singer')
route.register('song',views.SongViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('students/', include('api.urls')),
    path('api/', include(route.urls)),
    # path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]
