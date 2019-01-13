from django.shortcuts import render, get_object_or_404
from sistemaRecomendacion_app.loadBD_V2 import populatePuntuaciones
from sistemaRecomendacion_app.forms import LibroForm, UsuarioForm
from sistemaRecomendacion_app.models import Libro, Usuario, Puntuacion
from sistemaRecomendacion_app.recommendations import  transformPrefs, calculateSimilarItems, getRecommendedItems, topMatches
import shelve

# Create your views here.


def index(request): 
    return render(request,'index.html')
 
def populateDB(request):
    populatePuntuaciones() 
    return render(request,'populate.html')


def loadRS(request):
    Prefs={}   # matriz de usuarios y puntuaciones a cada a items
    shelf = shelve.open("dataRS.dat")
    puntuacion = Puntuacion.objects.all()
    for p in puntuacion:
        usuario = int(p.usuario.idUsuario)
        libro = int(p.libro.isbn)
        puntuacion = float(p.puntuacion)
        Prefs.setdefault(user, {})
        Prefs[usuario][libro] = puntuacion
    shelf['Prefs']=Prefs
    shelf['ItemsPrefs']=transformPrefs(Prefs)
    shelf['SimItems']=calculateSimilarItems(Prefs, n=10)
    shelf.close()
    
#APARTADO A
def search(request):
    if request.method=='GET':
        form = LibroForm(request.GET, request.FILES)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            libro = get_object_or_404(Libro, pk=isbn)
            return render(request,'ratedLibro.html', {'libro':libro})
    form=LibroForm()
    return render(request,'buscarLibro.html', {'form':form })


#APARTADO C
def recomendar(request):
    if request.method=='GET':
        form = UsuarioForm(request.GET, request.FILES)
        if form.is_valid():
            idUsuario = form.cleaned_data['idUsuario']
            usuario = get_object_or_404(Usuario, pk=idUsuario)
            return render(request,'inicio.html', {'usuario':usuario})
    form=LibroForm()
    return render(request,'recomendarLibro.html', {'form':form })



# APARTADO C/CON RECOMENDACION
def recomendarLibro(request):
    if request.method=='GET':
        form = UsuarioForm(request.GET, request.FILES)
        if form.is_valid():
            idUsuario = form.cleaned_data['idUsuario']
            usuario = get_object_or_404(Usuario, pk=idUsuario)
            shelf = shelve.open("dataRS.dat")
            Prefs = shelf['Prefs']
            SimItems = shelf['SimItems']
            shelf.close()
            rankings = getRecommendedItems(Prefs, SimItems, int(idUsuario))
            recommended = rankings[:2]
            items = []
            for re in recommended:
                item = Libro.objects.get(pk=re[1])
                items.append(item)
            return render(request,'recommendationItems.html', {'usuario': usuario, 'items': items})
    form = UsuarioForm()
    return render(request,'recomendarLibro.html', {'form': form})


