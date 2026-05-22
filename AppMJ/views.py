from django.shortcuts import render
from .models import Album

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def legado(request):
    return render (request, 'index2.html')

def albumes(request):
    albumes_list = Album.objects.all().order_by('anio_lanzamiento')
    return render(request, 'index3.html', {'albumes': albumes_list})