from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario=models.IntegerField(primary_key=True, verbose_name="Usuario id", unique=True)
    edad=models.IntegerField(verbose_name="edad")
    localizacion=models.CharField(max_length=80)

class Libro(models.Model):
    isbn=models.CharField(primary_key=True,max_length=50, verbose_name="Libro id", unique=True)
    titulo=models.CharField(max_length=80)
    autor=models.CharField(max_length=80)
    año_publicacion=models.IntegerField(verbose_name="Año publicacion")
    editor=models.CharField(max_length=80)
    urls=models.CharField(max_length=200)

class Puntuacion(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    puntuacion=models.IntegerField(verbose_name="Puntuacion")