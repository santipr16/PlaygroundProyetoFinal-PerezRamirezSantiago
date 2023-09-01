from django import forms
from .models import Alumno, Profesor, Instrumento, Foto, Comentario

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'direccion', 'correo', 'telefono', 'foto']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'direccion', 'correo', 'telefono', 'foto']

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['tipo', 'modelo', 'marca', 'año', 'foto' ]

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['imagen']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']