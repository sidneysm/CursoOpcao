from django import forms
from .models import *

class AlunoForms(forms.ModelForm):
	senha = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Aluno
		fields = ('nome', 'endereco', 'data_de_nascimento', 'email', 'senha',)