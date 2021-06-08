import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Curso, Adidas
from django.http import Http404


def index ( request ):
    x = 7 / 0

def cursos (request):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)

def nuevo_curso(request): #obtiene los datos ingresados en FormularioCurso y los inserta en el modelo Curso
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST) #crea una instancia de forms
        if form.is_valid():  #validacion  
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso()
    ctx = {"form": form}
    return render(request, "myapp/nuevo_curso.html", ctx)
            
   
def cursos_json(request):
    response = JsonResponse(list(Curso.objects.values()), safe=False)
    return response  

def curso(request, nombre):
    try:
        curso = Curso.objects.post(nombre= nombre)
    except Curso.DoesNotExist:
        raise Http404
    ctx = {"curso": curso}
    return render(request, "myapp/curso.html", ctx)

def compraZapatillas(request):
    if request.method == 'POST':
        if(request.POST['boton1'] == '39'):
            zapatilla = Adidas(articulo="ADIDAS ZX", talle = '39')
            zapatilla.save()
            boton1 = request.POST['boton1']
            ctx = {
                'boton1' : boton1,
            } 
            return render(request, 'myapp/adidas.html', ctx)
        if(request.POST['boton1'] == '40'):
            zapatilla = Adidas(articulo="ADIDAS ZX", talle = '40')
            zapatilla.save()
            boton2 = request.POST['boton1']
            ctx1 = {
                'boton2' : boton2,
            }
            return render(request, 'myapp/adidas.html', ctx1)
        if(request.POST['boton1'] == '42'):
            zapatilla = Adidas(articulo="ADIDAS ZX", talle = '42')
            zapatilla.save()
            boton3 = request.POST['boton1']
            ctx2 = {
                'boton3' : boton3,
            }
            return render(request, 'myapp/adidas.html', ctx2)
        if(request.POST['boton1'] == '44'):
            zapatilla = Adidas(articulo="ADIDAS ZX", talle = '44')
            zapatilla.save()
            boton4 = request.POST['boton1']
            ctx3 = {
                'boton4' : boton4,
            }
            return render(request, 'myapp/adidas.html', ctx3)
    ctx = {
        'boton1' : '',
        'boton2' : '',
        'boton3' : '',
        'boton4' : ''
    }
    return render(request, 'myapp/adidas.html')
    
    
   
   
def listaComprada(request):
    zapatillas = Adidas.objects.all()
    ctx = {"zapatillas": zapatillas}
    return render(request, 'myapp/salidaAdidas.html', ctx)





