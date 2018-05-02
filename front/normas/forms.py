from django import forms
from .models import Norma


class NormaForm(forms.ModelForm):
    class Meta:
        model = Norma
        fields = ['norm_text', 'idioma', 'pretag','texto_etiquetado', 'aprobacion_etiquetado' , 'observaciones_etiquetado']

        widgets = {
            'norm_text': forms.Textarea(attrs={'class': 'form-control'}),
            'idioma': forms.Select(attrs={'class': 'form-control'}),
            'pretag': forms.Select(attrs={'class': 'form-control'}),
            'texto_etiquetado': forms.Textarea(attrs={'class': 'form-control'}),
            'aprobacion_etiquetado': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'observaciones_etiquetado': forms.Textarea(attrs={'class': 'form-control'}),
        }
   