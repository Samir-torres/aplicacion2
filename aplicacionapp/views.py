from django.shortcuts import render
from infor.models import Categinfor, Bibliografiainfor
from django.db import models
from django.http import HttpResponse
from mate.models import Categmate, Bibliografiamate
from electronica.models import Categelectro, Bibliografiaelectro

def home(request):
    return render(request, "aplicacionapp/home.html")

def buscar(request):

    if  request.GET["links"]:


        link = request.GET["links"]
        
        if len(link) > 50:

            mensaje = "Texto demasiado largo"

        else:
            infor = Bibliografiainfor.objects.filter(titulo__icontains= link)
            mates = Bibliografiamate.objects.filter(titulo__icontains= link)
            electros = Bibliografiaelectro.objects.filter(titulo__icontains= link)

            if not (infor or mates or electros):
                return render (request, "aplicacionapp/negacion.html", {"query":link})

            return render(request, "aplicacionapp/resultados.html", {"infor":infor, "mates":mates, "electros":electros, "query":link})

    else:
        mensaje= "No has introducido nada"

    return HttpResponse(mensaje)

# Create your views here.
