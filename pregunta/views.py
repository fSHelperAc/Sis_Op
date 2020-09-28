from django.shortcuts import render
import re
import random
from .models import Pregunta
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

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
    return render(request,'pregunta/detail.html',{'pregunta': pregunta})

def populate(request):
    pregs = []
    with open('Preguntas.txt', 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', '')
        data_S  =  re.compile("[0-9]*\.-").split(data)
        
        for i in data_S:
            if len(i) < 10:
                continue
            pp = PreguntaP(i)

            new_entry = Pregunta(pregunta_s =pp.p)
            new_entry.respuesta_a= pp.r[0]
            new_entry.respuesta_b= pp.r[1]
            new_entry.respuesta_c= pp.r[2]
            new_entry.resp_c = pp.r_c
            new_entry.save()
    return render(request,'pregunta/temp.html',{})

def go_to_random(request):
    preguntas = Pregunta.objects.all()
    preg = random.choice(preguntas)
    return redirect('pregunta:pregunta_detail', pk=preg.pk)
