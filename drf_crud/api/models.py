from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    stdclass = models.IntegerField(blank=True)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']