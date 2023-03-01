from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create models here.
class Singer(models.Model):
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20)
    class Meta:
        ordering = ('id',)
    # def __str__(self):
    #     return str(self.roll)
    def __str__(self):
        return self.name
    

class Song(models.Model):
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE, related_name='sungby')
    title = models.CharField(max_length=150,blank=False)
    duration = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(20.0)])
    

    def __str__(self):
        return self.singer.name