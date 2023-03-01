from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,error_messages={'required': 'Please enter your name'})
    roll = models.IntegerField()
    city = models.CharField(max_length=120)
    
    class Meta:
        ordering = ('id',)
    
    
    