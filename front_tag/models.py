from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Norma(models.Model):
    id              = models.AutoField(primary_key=True)
    norm_text       = models.TextField()
    fecha_creacion  = models.DateTimeField(auto_now=True)
    norm_url        = models.CharField(max_length=10000)
    INGLES          = 'EN'
    ESPANOL         = 'ES'
    FRANCES         = 'FR'
    PORTUGUES       = 'PR'
    LANG_CHOICES    = ((INGLES,    'Inglés'),
                       (ESPANOL,   'Español'),
                       (FRANCES,   'Frances'),
                       (PORTUGUES, 'Portugues'))

class Etiqueta(models.Model):
    id              = models.AutoField(primary_key=True)
    nombre          = models.TextField()
    etiqueta_text   = models.CharField(max_length=10000)
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