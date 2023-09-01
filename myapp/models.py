from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos/')
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos/')
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Instrumento(models.Model):
    tipo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    año = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/')

class Foto(models.Model):
    imagen = models.ImageField(upload_to='fotos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    contenido = models.TextField()