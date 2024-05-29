from django.shortcuts import render
from django.http import HttpResponse
# alummno/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Alumno, Curso, NotasPorCurso
from .forms import AlumnoForm, CursoForm, NotasPorCursoForm

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alummno/alumno_list.html'

class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'alummno/alumno_detail.html'

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alummno/alumno_form.html'
    success_url = reverse_lazy('alumno-list')

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alummno/alumno_form.html'
    success_url = reverse_lazy('alumno-list')

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'alummno/alumno_confirm_delete.html'
    success_url = reverse_lazy('alumno-list')

class CursoListView(ListView):
    model = Curso
    template_name = 'alummno/curso_list.html'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'alummno/curso_detail.html'

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'alummno/curso_form.html'
    success_url = reverse_lazy('curso-list')

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'alummno/curso_form.html'
    success_url = reverse_lazy('curso-list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'alummno/curso_confirm_delete.html'
    success_url = reverse_lazy('curso-list')

# class NotasPorCursoListView(ListView):
#     model = NotasPorCurso
#     template_name = 'alummno/notasporcurso_list.html'

# class NotasPorCursoDetailView(DetailView):
#     model = NotasPorCurso
#     template_name = 'alummno/notasporcurso_detail.html'
