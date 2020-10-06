from django.db import models

from django.urls import reverse

from django.utils import timezone

class Respuesta(models.Model):
    texto = models.CharField(max_length = 255)
    #TODO Corregir el null True por un dewfault value
    pregunta_k = models.ForeignKey('pregunta.Pregunta', on_delete=models.CASCADE, related_name='pregunta',  null=True)

    es_correcta = models.BooleanField(default=False)

    objects = models.Manager() 

    def __str__(self):
        return self.texto

    def set_correcta(self):
        self.es_correcta = True
        self.save()
    
class Pregunta(models.Model):

    pregunta_s = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)

    created = models.DateTimeField(default=timezone.now)
    #TODO Corregir el null True por un dewfault value
    cuestionario_k = models.ForeignKey('pregunta.Cuestionario', on_delete=models.CASCADE, related_name='cuestionario', null=True)

    objects = models.Manager()

    def __str__(self):
        return self.pregunta_s

    def get_next_url(self):
        return reverse('pregunta:go_to_next', args=[self.pk])
    def get_previous_url(self):
        return reverse('pregunta:go_to_previous', args=[self.pk])
    def get_absolute_url(self):
        return reverse('pregunta:pregunta_detail',args=[self.pk])

class Topic(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Cuestionario(models.Model):
    name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)


    topico_k = models.ForeignKey('pregunta.Topic',on_delete=models.SET_NULL, related_name='topic', blank=True, null=True)
    

    created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('pregunta:preguntas_list',args=[self.pk])

    def __str__(self):
        return self.name




