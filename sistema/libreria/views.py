from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request): #respuesta directa
    return HttpResponse("<h1>Bienvenido a biblioteca</h1>")
def nosotros(request): #respuesta directa con render html
    return render(request, 'paginas/nosotros.html')
