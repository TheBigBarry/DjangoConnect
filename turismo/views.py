from django.shortcuts import render, redirect
#Importar modelos de alumno
from .models import Alumno,Genero

# Create your views here.
def login(request):
    return render(request, 'login.html')


def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'index.html', context)
