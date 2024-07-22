from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Sanchez_Tucta_Persona

# Create your views here.


layout = """
    <h1> Proyecto Web (LP3 - 2024) | Sanchez tucta </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    return render(request,'index.html')


def saludo(request):
    return render(request,'saludo.html')

def persona(request):
    return render(request,'persona.html')

def crear_persona(request,nombre,apellido,sexo,fecha_de_registro):
    Sanchez_Tucta_Persona = Sanchez_Tucta_Persona(
        nombre = "Juan",
        apellido = "Torres Marques",
        sexo = "M",
        fecha_de_registro = True
    )
    Sanchez_Tucta_Persona.save()
    return HttpResponse(f"Persona Creada: {Sanchez_Tucta_Persona.nombre} - {Sanchez_Tucta_Persona.apellido} - {Sanchez_Tucta_Persona.sexo} - {Sanchez_Tucta_Persona.fecha_de_registro}")


