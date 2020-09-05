from django.shortcuts import render
from infor.models import Categinfor, Bibliografiainfor
from django.db import models
from django.http import HttpResponse

def infor(request):

    categorias = Categinfor.objects.all()
    biblio = Bibliografiainfor.objects.all()

    return render(request, "infor/infor.html", {"biblio": biblio, "categorias": categorias})


