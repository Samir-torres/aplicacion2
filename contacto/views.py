from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings 
from contacto.forms import Formulario


def contacto(request):


    if request.method == "POST":
        miformulario = Formulario(request.POST)

        if miformulario.is_valid():
            info = miformulario.cleaned_data

            send_mail(info['asunto'], info['mensaje'], info.get('email',''), ['riossamir39@hotmail.com'])
        
            return render(request, "contacto/gracias.html")

    else:
        miformulario = Formulario()
    
    return render(request, "contacto/formulario.html", {"form":miformulario})
# Create your views here.
