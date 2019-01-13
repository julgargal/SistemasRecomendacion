# -*- encoding: utf-8 -*-
from django import forms

class LibroForm(forms.Form):
    isbn = forms.CharField(label='Libro id')
