from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'alias', 'ciudad', 'direccion', 'telefono', 'activo']  # Excluye 'puntuacion'
        widgets = {
            'ciudad': forms.Select(attrs={'class': 'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Si el formulario es de creación (no edición)
            self.instance.puntuacion = 'bueno'  # Asigna el valor predeterminado en la instancia
