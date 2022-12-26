from .models import Lanzamiento
from django import forms

class LanzamientoForm(forms.ModelForm):
    
    class Meta:
        model = Lanzamiento
        fields = (
            'foto',
            'nombre',
            'plataforma',
            'fecha',
            'descripcion'
        )
        labels = {
            'foto':'Imagen',
            'nombre':'Nombre',
            'plataforma':'Plataforma',
            'fecha':'Fecha de lanzamiento',
            'descripcion':'Descripción'
        }
        '''widgets = {
            #'foto':forms.FileInput(attrs={'class':'campo_input','type':'file'}),
            'nombre':forms.TextInput(attrs={'class':'campo_input'}),
            'plataforma':forms.Select(choices="PLATAFORMA", attrs={'class':'campo_input'}),
            'fecha':forms.DateField(attrs={'class':'campo_input'}),
            'descripcion':forms.Textarea(attrs={'class':'campo_input'}),
        }'''
