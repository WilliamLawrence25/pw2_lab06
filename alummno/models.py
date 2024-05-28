from django.db import models

# Create your models here.
class Alumno(models.Model):
    name = models.CharField(max_length=100)
    lastaname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} {self.lastaname}"

class Curso(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.teacher_name}"
    
class NotasPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.alumno} - {self.curso} - {self.nota}"