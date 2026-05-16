from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def legado(request):
    return render (request, 'index2.html')

def albumes(request):
    return render(request, 'index3.html')