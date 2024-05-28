from django.contrib import admin
from .models import *

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(NotasPorCurso)
class NotasPorCurso(admin.ModelAdmin):
    pass