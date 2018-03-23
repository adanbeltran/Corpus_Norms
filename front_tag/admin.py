from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Norma, Etiqueta,Atributo,Etiquetado

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Norma)
admin.site.register(Etiqueta)
admin.site.register(Atributo)
admin.site.register(Etiquetado)