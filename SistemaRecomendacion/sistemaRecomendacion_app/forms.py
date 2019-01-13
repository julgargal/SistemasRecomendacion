# -*- encoding: utf-8 -*-
from django import forms

class LibroForm(forms.Form):
    isbn = forms.CharField(label='Libro id')
    
class UsuarioForm(forms.Form):
    idUsuario = forms.CharField(label='Usuario id')
