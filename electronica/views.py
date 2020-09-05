from django.shortcuts import render, HttpResponse
from electronica.models import Categelectro, Bibliografiaelectro
from django.db import models

def electronica(request):

    categorias = Categelectro.objects.all()
    biblio = Bibliografiaelectro.objects.all()

    return render(request, "electronica/electronica.html", {"biblio": biblio, "categorias": categorias})

# Create your views here.
