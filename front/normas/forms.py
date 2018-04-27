from django import forms
from .models import Norma


class NormaForm(forms.ModelForm):
    class Meta:
        model = Norma
        fields = ['norm_text', 'idioma', 'pretag']