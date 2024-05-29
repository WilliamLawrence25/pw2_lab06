# alumno/urls.py
from django.urls import path
from .views import (
    AlumnoListView,
    AlumnoCreateView,
    AlumnoUpdateView,
    AlumnoDeleteView,
    AlumnoDetailView,
    CursoListView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView,
    CursoDetailView,
)

urlpatterns = [
    path('alumnos/', AlumnoListView.as_view(), name='alumno-list'),
    path('alumnos/new/', AlumnoCreateView.as_view(), name='alumno-create'),
    path('alumnos/<int:pk>/', AlumnoDetailView.as_view(), name='alumno-detail'),
    path('alumnos/<int:pk>/edit/', AlumnoUpdateView.as_view(), name='alumno-edit'),
    path('alumnos/<int:pk>/delete/', AlumnoDeleteView.as_view(), name='alumno-delete'),
    
    path('cursos/', CursoListView.as_view(), name='curso-list'),
    path('cursos/new/', CursoCreateView.as_view(), name='curso-create'),
    path('cursos/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
    path('cursos/<int:pk>/edit/', CursoUpdateView.as_view(), name='curso-edit'),
    path('cursos/<int:pk>/delete/', CursoDeleteView.as_view(), name='curso-delete'),

    # path('notas/', NotasPorCursoListView.as_view(), name='notas-list'),
    # path('notas/new/', NotasPorCursoCreateView.as_view(), name='notas-create'),
    # path('notas/<int:pk>/', NotasPorCursoDetailView.as_view(), name='notas-detail'),
    # path('notas/<int:pk>/edit/', NotasPorCursoUpdateView.as_view(), name='notas-edit'),
    # path('notas/<int:pk>/delete/', NotasPorCursoDeleteView.as_view(), name='notas-delete'),
]
