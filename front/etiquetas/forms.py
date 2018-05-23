from django import forms
from django.apps import apps



class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('normas','Etiqueta')
        fields = ['nombre' , 'etiqueta_text' , 'activa']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta_text': forms.Textarea(attrs={'class': 'form-control', 'rows':'2'}),
            'activa': forms.CheckboxInput(attrs={'class': 'form-control'}),
         }