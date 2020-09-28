from django.db import models

from django.urls import reverse

class Pregunta(models.Model):

    pregunta_s = models.CharField(max_length = 255)
    respuesta_a = models.CharField(max_length = 255)
    respuesta_b = models.CharField(max_length = 255)
    respuesta_c = models.CharField(max_length = 255)

    resp_c = models.CharField(max_length = 100)

    objects = models.Manager() # The default manager.

    def __str__(self):
        return self.pregunta_s

    def get_absolute_url(self):
        return reverse('pregunta:pregunta_detail',args=[ self.pk])
