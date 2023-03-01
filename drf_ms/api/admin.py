from django.contrib import admin
from . models import Singer,Song
# Register your models here.
# admin.site.register(Singer)
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['name','gender']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title','duration']