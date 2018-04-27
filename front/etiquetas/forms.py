from django import forms
from django.apps import apps



class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('normas','Etiqueta')
        fields = ['nombre' , 'etiqueta_text' , 'activa']