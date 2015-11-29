from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from curso.util import CPF

class AlunoForms(UserCreationForm):
	#cpf = forms.CharField()
	class Meta:
		model = Aluno
		
		fields = ('username', 'first_name', 'last_name', 'cpf','endereco', 'data_de_nascimento', 'email', )

	def clean_cpf(self):
		cd = self.cleaned_data
		cpf = cd.get('cpf')
		
		cpf_vaol = CPF(cpf)

		if not cpf_vaol.isValid():
			raise forms.ValidationError("CPF inválido")
		return cpf_vaol

	# def clean(self):
	# 	cd = self.cleaned_data