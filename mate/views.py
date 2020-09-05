from django.shortcuts import render, HttpResponse
from mate.models import Categmate, Bibliografiamate
from django.db import models

def mate(request):

    categorias = Categmate.objects.all()
    biblio = Bibliografiamate.objects.all()

    return render(request, "mate/mate.html", {"biblio": biblio, "categorias": categorias})

# Create your views here.
