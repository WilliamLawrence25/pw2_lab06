from django.db import models

# Create your models here.
class Alumno(models.Model):
    name = models.CharField(max_length=100)
    lastaname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} {self.lastaname}"