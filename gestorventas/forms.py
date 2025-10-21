from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['vendedor', 'fecha', 'monto']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'vendedor': forms.Select(attrs={'class': 'form-select'}),
        }