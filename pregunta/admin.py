from django.contrib import admin

from .models import Pregunta, Respuesta, Topic, Cuestionario

# Register your models here.
admin.site.register(Respuesta)
admin.site.register(Pregunta)
admin.site.register(Topic)
admin.site.register(Cuestionario)