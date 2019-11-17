from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= Cliente
        fields= ['nombre', 'rut', 'email', 'celular', 'contraseña']

