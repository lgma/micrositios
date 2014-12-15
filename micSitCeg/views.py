from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from micSitCeg.models import Interesados
from django.template import RequestContext
from micSitCeg.forms import InteresadosForm
from datetime import timezone
from django.core.context_processors import csrf

# Create your views here.
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('micSitCeg/index.html', c,  content_type="text/html")

def interesado_create(request):
    if request.method == 'POST':
        form = InteresadosForm(request.POST)
        if form.is_valid():
            interesados = Interesados (
                nombres = form.cleaned_data['nombre'],
                apellidoPaterno = form.cleaned_data['apellido'],
                email = form.cleaned_data['email'],
                telefono = form.cleaned_data['telefono'],
                extension = form.cleaned_data['extension'],
                celular = form.cleaned_data['celular'],
                fecha = timezone.now())
            interesados.save()
            return render_to_response('micSitCeg/gracias.html', {}, content_type="text/html")
        else:
            #form =InteresadosForm()
            #return render_to_response('micSitCeg/index.html', {},  content_type="text/html")
            return redirect('/micrositios/')
    else:
        return redirect('/micrositios/nopost')