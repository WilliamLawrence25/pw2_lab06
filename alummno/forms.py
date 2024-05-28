from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['name', 'lastname', 'age']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['name', 'teacher_name']

class NotasPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotasPorCurso
        fields = ['alumno', 'curso', 'nota']
