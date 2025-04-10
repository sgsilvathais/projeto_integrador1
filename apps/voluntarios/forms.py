from django import forms
from .models import Voluntario

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome', 'email', 'telefone', 'endereco', 'cidade', 'area']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '99999-9999'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Logradouro, nº, complemento'}),
            'cidade': forms.RadioSelect(choices=[
                ('São José dos Campos', 'São José dos Campos'),
                ('Jacareí', 'Jacareí'),
                ('Caçapava', 'Caçapava'),
                ('Taubaté', 'Taubaté'),
            ]),
            'area': forms.RadioSelect(choices=[
                ('Feira de adoção', 'Feira de adoção'),
                ('Cuidados e Bem-Estar', 'Cuidados e Bem-Estar'),
                ('Outras tarefas', 'Outras tarefas'),
            ]),
        }
