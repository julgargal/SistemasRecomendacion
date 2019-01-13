#encoding:utf-8
import csv
import os
import django
import sys
# Muy importantes las dos líneas siguientes, sino da un error de que no encuentra la app "movies"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SistemaRecomendacion.settings")
django.setup()
from sistemaRecomendacion_app import models

def populatePuntuaciones():
    models.Usuario.objects.all().delete()
    models.Libro.objects.all().delete()
    models.Puntuacion.objects.all().delete()


    with open('C:\\Users\\maria\\Eclipse\\workspaceSR\\SistemasRecomendacion\\SistemaRecomendacion\\docs\\BX-Book-Ratings.csv', encoding='latin-1') as File:
        count=1
        reader = csv.reader(File, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        row = next(reader)
        for row in reader:
            if count < 5:
                idUsuario_BUENO = row[0]
                isbLibro_BUENO = row[1]
                puntuacion = row[2]



                # usuario= models.Usuario.objects.get(idUsuario=idUsuario)
                # todos_usuarios=models.Usuario.objects.all()

                with open('C:\\Users\\maria\\Eclipse\\workspaceSR\\SistemasRecomendacion\\SistemaRecomendacion\\docs\\docs/BX-Users.csv', encoding='latin-1') as File:
                    reader_usuarios = csv.reader(File, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                    row_usuarios = next(reader_usuarios)
                    for row_usuarios in reader_usuarios:
                        idUsuario = row_usuarios[0]
                        localizacion = row_usuarios[1]
                        if row_usuarios[2] == "NULL":
                            edad = int(0)
                        else:
                            edad = row_usuarios[2]

                        if idUsuario_BUENO == idUsuario:
                            if models.Usuario.objects.filter(idUsuario=idUsuario_BUENO).count()==0:
                                usuario = models.Usuario(idUsuario=idUsuario, edad=edad, localizacion=localizacion)
                                usuario.save()
                                print("Usuario con id: "+str(idUsuario)+" cargado.")
                        #sys.stdout.write('\r' + "Usuario con id: " + str(count))
                        #sys.stdout.flush()


                with open('C:\\Users\\maria\\Eclipse\\workspaceSR\\SistemasRecomendacion\\SistemaRecomendacion\\docs\\docs/BX-Books.csv', encoding='latin-1') as File:
                    reader_libros = csv.reader(File, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                    row_libros = next(reader_libros)
                    for row_libros in reader_libros:
                        libroId = row_libros[0]
                        if isbLibro_BUENO == libroId:
                            if models.Libro.objects.filter(isbn=isbLibro_BUENO).count()==0:
                                titulo = row_libros[1]
                                autor = row_libros[2]
                                año_publicacion = row_libros[3]
                                editor = row_libros[4]

                                url_1 = row_libros[5]
                                url_2 = row_libros[6]
                                url_3 = row_libros[7]
                                urls = url_1 + " , " + url_2 + " , " + url_3

                                libro = models.Libro(isbn=libroId, titulo=titulo, autor=autor,
                                         año_publicacion=año_publicacion, editor=editor, urls=urls)
                                libro.save()
                                print("Libro con id: " + str(isbLibro_BUENO) + " cargado.")

                #Comprobamos que el libro y los usuarios existan
                Nusuario = models.Usuario.objects.filter(idUsuario=idUsuario_BUENO).count()
                Nlibro = models.Libro.objects.filter(isbn=isbLibro_BUENO).count()

                if(Nusuario+Nlibro==2):
                    usuario = models.Usuario.objects.get(idUsuario=idUsuario_BUENO)
                    libro = models.Libro.objects.get(isbn=isbLibro_BUENO)


                    puntuacion = models.Puntuacion(usuario=usuario, libro=libro, puntuacion=puntuacion)
                    puntuacion.save()
                    sys.stdout.write('\r' + "Puntuaciones cargadas: " + str(count))
                    count = count + 1
                    sys.stdout.flush()
                    print("\n")

    print("\n")
    print("Se han cargado: " + str(count) + " puntuaciones.")

populatePuntuaciones()