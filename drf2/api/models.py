from django.db import models

# Create models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank=True)
    roll = models.IntegerField(blank=False)
    city = models.CharField(max_length=200)
    class Meta:
        ordering = ('id',)
    # def __str__(self):
    #     return str(self.roll)

