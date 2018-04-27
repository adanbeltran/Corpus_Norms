from django.db import models
from django.utils import timezone
from django.core.files import File
import csv
import datetime

class Norma(models.Model):
    items=[]
    TAG_CHOICES=[]
    myList=()
    id              = models.AutoField(primary_key=True)
    norm_text       = models.TextField()
    fecha_creacion  = models.DateTimeField(auto_now=True)
    norm_url        = models.CharField(max_length=10000)
    INGLES          = 'EN'
    ESPANOL         = 'ES'
    FRANCES         = 'FR'
    PORTUGUES       = 'PR'
    LANG_CHOICES    = ((INGLES,'Ingles'),(ESPANOL,'Espanol'),(FRANCES,'Frances'),(PORTUGUES,'Portugues'))
    l = list(myList)
    with open('/Users/ivan/PycharmProjects/front/normas/static/tag/option_tag.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        line = 0 
        for row in reader:
            items.append(row)
            myList = list(items)
    for tag in items:
        TAG_CHOICES.append([tag[0] , tag[1]])
    
    idioma          = models.CharField(max_length=20,choices=LANG_CHOICES , default=ESPANOL )
    pretag          = models.CharField(max_length=100,choices=TAG_CHOICES , default=TAG_CHOICES[0][0] )
                  
    def __str__(self):
        norm_text= 'ssss'
        return self.norm_text

class Etiqueta(models.Model):
    id              = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=500)
    etiqueta_text   = models.TextField()
    fecha_creacion  = models.DateTimeField(auto_now=True)
    activa          = models.BooleanField("Activa", default=True)

class Atributo(models.Model):
    id              = models.AutoField(primary_key=True)
    etiqueta_id     = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    nombre_parametro= models.TextField()
    ENTERO          = 'INT'
    TEXTO           = 'TEXT'
    BOLEANO         = 'BOOL'
    ETIQUETA        = 'TAG'
    TIPO_CHOICES    = ((ENTERO,   'Entero'),
                       (TEXTO,    'Texto'),
                       (BOLEANO,  'Boleano'),
                       (ETIQUETA, 'Etiqueta'))
    atributo_id     = models.BigIntegerField(default=0, db_index=True)
    COND_AND        = 'AND'
    COND_OR         = 'OR'
    COND_CHOICES    = ((COND_AND, 'Y'),
                       (COND_OR, 'O'))
    orden           = models.BigIntegerField(default=0)

    def __str__(self):
        return self.nombre_parametro

class Etiquetado(models.Model):
    id              = models.AutoField(primary_key=True)
    etiqueta_id     = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    norma_id        = models.ForeignKey(Norma, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now=True)
    valor_parametro = models.TextField()
    COND_AND        = 'AND'
    COND_OR         = 'OR'
    COND_CHOICES    = ((COND_AND,   'Y'),
                       (COND_OR,    'O'))
    
    version         = models.BigIntegerField()
    orden = models.BigIntegerField(default=0)