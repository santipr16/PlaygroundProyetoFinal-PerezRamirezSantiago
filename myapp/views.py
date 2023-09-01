from django.shortcuts import render, redirect
from .models import *
from .forms import *
from . import views


def home(request):
    return render(request,'home')

def index(request):
    return render(request, 'login/index')


def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listado_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listado_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

def listado_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listado_alumnos.html', {'alumnos': alumnos})

def listado_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'listado_profesores.html', {'profesores': profesores})

def listado_instrumentos(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'listado_instrumentos.html', {'instrumentos': instrumentos})

def agregar_instrumento(request):
    if request.method == 'POST':
        form = InstrumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listado_instrumentos')
    else:
        form = InstrumentoForm()
    return render(request, 'agregar_instrumento.html', {'form': form})

def agregar_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fotos')
    else:
        form = FotoForm()
    return render(request, 'agregar_foto.html', {'form': form})

def foto(request):
    foto = Foto.objects.get()
    comentarios = foto.comentarios.all()
    if request.method == 'POST':
        form = Comentario(request.POST)
        if form.is_valid():
            comentarios = form.save(commit=False)
            comentarios.foto = foto
            comentarios.save()
            return redirect('fotos')
    else:
        form = Comentario()
    return render(request, 'fotos.html', {'fotos': foto, 'comentarios': comentarios, 'form': form})

def logout(request):
    logout(request)
    return redirect('index')
