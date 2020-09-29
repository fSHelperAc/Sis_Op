from django.db import models

from django.urls import reverse

from django.utils import timezone

class Respuesta(models.Model):
    pregunta = models.ForeignKey('pregunta.Pregunta', on_delete=models.CASCADE, related_name='pregunta')
    texto = models.CharField(max_length = 255)
    es_correcta = models.BooleanField(default=False)

    objects = models.Manager() 

    def set_correcta(self):
        self.es_correcta = True
        self.save()
    
    def __str__(self):
        return self.texto

    
class Pregunta(models.Model):

    pregunta_s = models.CharField(max_length = 255)

    author = models.CharField(max_length = 255)

    created = models.DateTimeField(default=timezone.now)

    objects = models.Manager() # The default manager.

    def __str__(self):
        return self.pregunta_s

    def get_next_url(self):
        return reverse('pregunta:go_to_next', args=[self.pk])
    def get_previous_url(self):
        return reverse('pregunta:go_to_previous', args=[self.pk])
    def get_absolute_url(self):
        return reverse('pregunta:pregunta_detail',args=[self.pk])
