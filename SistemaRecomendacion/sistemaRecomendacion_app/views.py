from django.shortcuts import render, get_object_or_404
#from sistemaRecomendacion_app.loadBD_V2 import populatePuntuaciones
from sistemaRecomendacion_app.forms import LibroForm
from sistemaRecomendacion_app.models import Libro

# Create your views here.


def index(request): 
    return render(request,'index.html')
 
# def populateDB(request):
#     populatePuntuaciones() 
#     return render(request,'populate.html')


def loadRS(request):
    loadDict()
    return render(request,'loadRS.html')
  
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
