#encoding:utf-8
import csv
import os
import django
import re
import time
import sys
import unicodedata

# Muy importantes las dos líneas siguientes, sino da un error de que no encuentra la app "movies"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SistemaRecomendacion.settings")
django.setup()
from sistemaRecomendacion_app import models




def populateLibros():
    models.Libro.objects.all().delete()

    count = 1
    with open('../docs/BX-Books.csv', encoding='latin-1') as File:
        reader = csv.reader(File, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        row=next(reader)
        for row in reader:
            if count < 300:
                libroId=row[0]
                titulo=row[1]
                autor=row[2]
                año_publicacion=row[3]
                editor=row[4]

                url_1=row[5]
                url_2=row[6]
                url_3=row[7]
                urls=url_1+" , "+url_2+" , "+url_3


                libro = models.Libro(isbn=libroId, titulo=titulo, autor=autor,
                                     año_publicacion=año_publicacion,editor=editor,urls=urls)
                libro.save()
                count = count + 1
                sys.stdout.write('\r' +"Peliculas cargadas: "+ str(count))
                sys.stdout.flush()
        print("\n")
        print("Se han cargado: "+str(count)+" libros")


def populateUsuarios():
    models.Usuario.objects.all().delete()

    count = 0
    with open('../docs/BX-Users.csv', encoding='latin-1') as File:
        reader = csv.reader(File, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        row=next(reader)
        for row in reader:
            if count <= 300:
                idUsuario=row[0]
                localizacion=row[1]
                if row[2]=="NULL":
                    edad=0
                else:
                    edad=row[2]

                usuario = models.Usuario(idUsuario=idUsuario, edad=edad, localizacion=localizacion)
                usuario.save()
                count = count + 1
                sys.stdout.write('\r' + "Usuarios cargados: " + str(count))
                sys.stdout.flush()
        print("\n")
        print("Se han cargado: " + str(count) + " usuarios.")

def populatePuntuaciones():
    models.Usuario.objects.all().delete()

    count = 1
    with open('../docs/BX-Book-Ratings.csv', encoding='latin-1') as File:
        reader = csv.reader(File, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        row=next(reader)
        for row in reader:
            if count < 100:
                idUsuario=row[0]
                usuario= models.Usuario.objects.get(idUsuario=idUsuario)
                todos_usuarios=models.Usuario.objects.all()

                isbn=row[1]
                libro=models.Libro.objects.get(isbn=isbn)
                todos_libros=models.Libro.objects.all()
                puntuacion=row[2]

                if usuario in todos_usuarios and libro in todos_libros:


                    puntuacion = models.Puntuacion(usuario=usuario, libro=libro, puntuacion=puntuacion)
                    puntuacion.save()
                    count = count + 1
                else:
                    count="Ninguno"
                sys.stdout.write('\r' + "Puntuaciones cargadas: " + str(count))
                sys.stdout.flush()
        print("\n")
        print("Se han cargado: " + str(count) + " puntuaciones.")


#populateLibros()
#populateUsuarios()
populatePuntuaciones()