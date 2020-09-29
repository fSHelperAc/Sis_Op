from django.shortcuts import render
import re
import random
from .models import Pregunta, Respuesta
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic import ListView

import logging


class PreguntaP:
    p = ""
    r = []
    r_c = ""
    def __init__(self, s):
        s_S = [x.strip() for x in re.compile("(a\)|b\)|c\))").split(s)]
        self.r_c, self.p, self.r = s_S[0][0], s_S[0][1:], [i+j for i,j in zip(s_S[1::2], s_S[2::2])]


def preguntas_list(request):
    preguntas = Pregunta.objects.all()
    return render(request,'home.html', {'preguntas': preguntas})

def pregunta_detail(request, pk):
    pregunta = get_object_or_404(Pregunta, pk=pk)
    respuesta = Respuesta.objects.filter(pregunta = pk)
    return render(request,'pregunta/detail.html',{'respuesta': respuesta,'pregunta': pregunta})

def populate(request):
    pregs = []
    with open('Preguntas.txt', 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', '')
        data_S  =  re.compile("[0-9]*\.-").split(data)
        
        for i in data_S:
            if len(i) < 10:
                continue
            pp = PreguntaP(i)

            entry_preg = Pregunta(pregunta_s =pp.p, author = "Erik")
            ii = 0
            varss = "ABC"
            entry_preg.save()
            for i in pp.r:
                entry_resp = Respuesta(pregunta=entry_preg, texto = i, es_correcta =  varss[ii]==pp.r_c)
                entry_resp.save()
                ii+=1
            
    return render(request,'pregunta/temp.html',{})

def go_to_random(request):
    preguntas = Pregunta.objects.all()
    preg = random.choice(preguntas)
    return redirect('pregunta:pregunta_detail', pk=preg.pk)

def go_to_next(request, pk):
    preg = Pregunta.objects.filter(pk__gt=pk).order_by('pk').first()
    return redirect('pregunta:pregunta_detail', pk=preg.pk)

def go_to_previous(request, pk):
    preg = Pregunta.objects.filter(pk__lt=pk).order_by('pk').last()
    return redirect('pregunta:pregunta_detail', pk=preg.pk)

def search(request):
    query = request.GET.get('search')
    if query:
        result = Pregunta.objects.filter(pregunta_s__contains=query)
    else:
        result = None
    return render(request,'pregunta/buscar.html',{'preguntas' : result})

       