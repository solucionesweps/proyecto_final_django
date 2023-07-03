from django.shortcuts import render
#Libreria que permite mostrar respuestas en formato http
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo cara...")

# Create your views here.
